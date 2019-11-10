#!/usr/bin/python
# coding:utf-8
import RPi.GPIO as gpio

from log import logger_creater

"""

the entrance grand

"""

import time
import traceback


class Entrancer(object):
    CLOSED = "closed"
    OPEND = "opend"

    def __init__(self,opened_pin,open_pin):
        self.logger = logger_creater.init_log(__name__)
        self.__opened_pin = opened_pin
        self.opend_time = time.time()
        self.__is_opened = False
        self.__open_pin = open_pin
        self.state = self.CLOSED
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.__opened_pin,gpio.IN,pull_up_down=gpio.PUD_UP)
        gpio.setup(self.__open_pin,gpio.OUT)
        gpio.add_event_detect(self.__opened_pin,gpio.RISING,callback=self.__check_entrancer)

    def __check_entrancer(self,channel):
        self.logger.info("entrancer rising up on %s",channel)
        try:
            if 0 == gpio.input(self.__opened_pin):
                self.__open_state()
            else:
                self.__close_state()
        except Exception,e:
            self.logger.info('Some error/exception occurred %s',e)
            self.logger.error(traceback.format_exc())

    def open(self):
        gpio.output(self.__open_pin,gpio.HIGH)
        self.__open_state()

    def __open_state(self):
        self.__is_opened = True
        self.opend_time = time.time()
        self.logger.info("entrancer opened by pin %d,",self.__opened_pin)
        self.state = self.OPEND

    def close(self):
        gpio.output(self.__open_pin,gpio.LOW)
        self.__close_state()

    def __close_state(self):
        self.logger.info("entrancer close by pin %d,",self.__opened_pin)
        self.__is_opened = False
        self.state = self.CLOSED
