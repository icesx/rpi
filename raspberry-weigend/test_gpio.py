# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import RPi.GPIO as gpio

import time
import traceback
def warn(channel):
    try:
        print channel," is not triger on ",channel,1
    except Exception,e:
        traceback.extract_stack()

def read(pin):
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin,gpio.IN,pull_up_down=gpio.PUD_UP)
    gpio.add_event_detect(pin,gpio.RISING,callback=lambda chanel: warn(chanel))

def setup(pin):
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin,gpio.OUT)
def write(pin,value):
    gpio.output(pin,value)
if __name__ == '__main__':
    d0=18
    read(d0)
    try:
        while True:
            print "while loop!!"
            time.sleep(1)
            time.sleep(1)
    finally:
        gpio.cleanup()