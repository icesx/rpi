#!/usr/bin/python
# coding:utf-8
import RPi.GPIO as gpio
import time
import traceback

from log import logger_creater
import math

NORMARL_OPEN_TIME_OUT = 6


class Controller:

    def __init__(self):
        self.logger = logger_creater.init_log(__name__)
        self.fence_fired_time_before = time.time() - 10000

    def __warn(self,alarm,communication):
        self.logger.info("try to warn...")
        alarm.do_beep()
        communication.warn()

    def __check_entrancer_alarm(self,reporter,alarm,entrancer):
        """

        :type alarm: alarm.alarm.Alarm
        :type entrancer: entrancer.entrancer.Entrancer
        """
        reciverInfo = reporter.heat_beat()
        self.logger.info("open or close reciver=%s",reciverInfo)
        if reciverInfo.is_open_long == True:
            alarm.disable()
            entrancer.open()
        if reciverInfo.is_open_once == True:
            entrancer.open()
            time.sleep(0.05)
            entrancer.close()
        if reciverInfo.close == True:
            entrancer.close()
            alarm.enable()
        self.logger.info("check_entrancer_alarm finish.")

    def control(self,communication,entrancer,alarm,fence):
        """

        :type communication:connection.communication.Communication
        :type entrancer: entrancer.entrancer.Entrancer
        :type alarm: alarm.alarm.Alarm
        :type fence:fence.fence.Fence

        """
        try:
            while True:
                try:
                    time.sleep(0.5)
                    self.logger.info("main loop....")
                    if (self.fence_fired_time_before != fence.fired_time):
                        # if fence is broken fence_fired_time is fence.fired_time awasy,then not to check warn!
                        self.fence_fired_time_before = fence.fired_time
                        if abs(fence.fired_time - entrancer.opend_time) >= NORMARL_OPEN_TIME_OUT:
                            self.__warn(alarm,communication)
                        else:
                            self.logger.info("fence fired but is not warn!")
                    else:
                        """
                        
                        fence befor time same with fence.fired_time,that's means fence is not work this time.
                        
                        """
                        self.logger.info(
                            "fence is not work this time.")
                    self.__check_entrancer_alarm(communication,alarm,entrancer)
                except Exception,e:
                    self.logger.error('Some error/exception occurred,%s',e)
                    self.logger.error(traceback.format_exc())
        except KeyboardInterrupt:
            self.logger.info("KeyboardInterrupt")
        finally:
            gpio.cleanup()
