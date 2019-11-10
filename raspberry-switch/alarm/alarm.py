# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import RPi.GPIO as gpio
import thread
import time

from log import logger_creater

BEEP_TIME=2

class Alarm(object):
    def __init__(self,pin):
        self.beep = pin
        self.__disable=False
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.beep,gpio.OUT)
        gpio.output(self.beep,gpio.LOW)
        self.logger=logger_creater.init_log(__name__)
    def do_beep(self):
        self.logger.info("alarm to beep on a thread...")
        thread.start_new_thread(self.__beep_on_thread,())

    def __beep_on_thread(self):
        if self.__disable:
            self.__close_beep()
        else:
            gpio.output(self.beep,gpio.HIGH)
            time.sleep(BEEP_TIME)
            gpio.output(self.beep,gpio.LOW)
        self.logger.info("beep thread is finished!")

    def __close_beep(self):
        gpio.output(self.beep,gpio.LOW)
        self.logger.info("alarm  beep was closed")

    def disable(self):
        self.__disable = True
        gpio.output(self.beep,gpio.LOW)
        self.logger.info("alarm is disabled")
    def enable(self):
        self.__disable = False
        self.logger.info("alarm is enabled")
