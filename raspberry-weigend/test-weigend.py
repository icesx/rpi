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
from weigend.weigend import weigend


def warn(channel,weigend):
    try:
        if gpio.input(channel) == 1:
            if channel == 15:
                weigend.set_bit(0)
            elif channel == 16:
                weigend.set_bit(1)
            else:
                print "not you", channel
        else:
            print channel," is not triger on ",channel,1
    except Exception,e:
        traceback.extract_stack()


def callback(weigendData):
    print weigendData.get_cardno()


_weigend = weigend(callback)


def read(warn_pin,weigend):
    gpio.setmode(gpio.BOARD)
    gpio.setup(warn_pin,gpio.IN,pull_up_down=gpio.PUD_DOWN)
    gpio.add_event_detect(warn_pin,gpio.RISING,callback=lambda chanel: warn(chanel,weigend))

def setup(pin):
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin,gpio.OUT)
def write(pin,value):
    gpio.output(pin,value)
if __name__ == '__main__':
    d0=15
    d1=16
    read(d0,_weigend)
    read(d1,_weigend)
    try:
        while True:
            print "while loop!!"
            time.sleep(1)
            time.sleep(1)
    finally:
        gpio.cleanup()
