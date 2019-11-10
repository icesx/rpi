# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import RPi.GPIO as gpio
import time
import traceback
"""

"""
if __name__ == '__main__':
    warn_pin = 11
    gpio.setmode(gpio.BOARD)
    gpio.setup(warn_pin,gpio.OUT)
    gpio.output(warn_pin,gpio.HIGH)
    time.sleep(0.1)
    gpio.output(warn_pin,gpio.LOW)
    print "opened"
    gpio.cleanup()