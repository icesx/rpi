#coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import RPi.GPIO as gpio
import time
if __name__ == '__main__':
    gpio.setmode(gpio.BOARD)
    channel=32
    i=0
    while True:
        i+=1
        gpio.setup(channel,gpio.IN)
        channel_trigerd=gpio.wait_for_edge(channel,gpio.RISING,timeout=5000)
        if channel_trigerd is None:
            print 'Timeout occurred'
        else:
            print 'Edge detected on channel',channel,i
            time.sleep(1)
