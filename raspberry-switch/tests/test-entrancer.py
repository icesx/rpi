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
    warn_pin = 10
    gpio.setmode(gpio.BOARD)
    gpio.setup(warn_pin,gpio.IN,pull_up_down=gpio.PUD_UP)
    while True:
        try:
            time.sleep(0.3)
            if gpio.input(warn_pin) == 0:
                print warn_pin," is triger"
            else:
                print warn_pin," is not triger"
        except Exception,e:
            traceback.extract_stack()