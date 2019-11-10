# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import sys
sys.path.append("/home/pi/raspberry-switch")
from entrancer.entrancer import Entrancer
import  time

if __name__ == '__main__':
    et = Entrancer(32)
    while True:
        print "Entrancer opened is %s"%et.is_open_befor()
        time.sleep(1)
