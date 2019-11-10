# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import RPi.GPIO as gpio
import time
import traceback

"""

"""
import time

def warn(channel):
    try:
        if gpio.input(warn_pin) == 0:
            print warn_pin," is triger on ",channel
        else:
            print warn_pin," is not triger on ",channel
    except Exception,e:
        traceback.extract_stack()


if __name__ == '__main__':
    warn_pin = 10
    gpio.setmode(gpio.BOARD)
    gpio.setup(warn_pin,gpio.IN,pull_up_down=gpio.PUD_UP)
    gpio.add_event_detect(warn_pin,gpio.RISING,callback=warn)
    try:
        while True:
            print "rising up!"
            time.sleep(10)
    finally:
        gpio.cleanup()
