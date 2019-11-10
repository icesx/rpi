#coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import RPi.GPIO as gpio
def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')

if __name__ == '__main__':
    gpio.setmode(gpio.BOARD)
    channel=32
    gpio.setup(channel,gpio.IN)
    while True:
        gpio.add_event_detect(channel,gpio.RISING,callback=my_callback)