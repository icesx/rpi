# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
# coding=utf-8
import RPi.GPIO as gpio
import time

from log import logger_creater

"""

"""


class Fence(object):
    def __init__(self,warn_pin):
        self.fired_time=time.time()
        self.logger = logger_creater.init_log(__name__)
        self.logger.info("init fence on pin %s",warn_pin)
        self.warn_pin = warn_pin
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.warn_pin,gpio.IN,pull_up_down=gpio.PUD_UP)
        gpio.add_event_detect(self.warn_pin,gpio.RISING,callback=self.__fire_fence)

    def __fire_fence(self,channel):
        if gpio.input(self.warn_pin) == 0:
            self.logger.info('Fence fired! on %s ',channel)
            self.fired_time=time.time()
        else:
            self.logger.info('Fence normarl on %s ',channel)
