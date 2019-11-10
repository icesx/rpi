# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import sys
import time
sys.path.append("/home/pi/raspberry-switch")
from status.status import PiStatus

if __name__ == '__main__':
    ps=PiStatus()
    time.sleep(2)
    print ps.cpu_temperature
    print ps.id
    print ps.uptime
    print ps.ip
