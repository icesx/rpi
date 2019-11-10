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
    if gpio.input(warn_pin) == 0:
        print warn_pin," fence is triger",time.time()
    else:
        print warn_pin," fence is not triger"


if __name__ == '__main__':
    warn_pin = 36
    gpio.setmode(gpio.BOARD)
    gpio.setup(warn_pin,gpio.IN,pull_up_down=gpio.PUD_UP)
    gpio.add_event_detect(warn_pin,gpio.RISING,callback=warn)
    while True:
        time.sleep(60)
        print "loop"
    gpio.cleanup()
