# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import os
import re
import thread
import time
import traceback
from log import logger_creater


class PiStatus(object):
    def __init__(self):
        self.logger = logger_creater.init_log(__name__)
        self.id = self.__cpu_id()
        self.cpu_temperature="-100"
        self.uptime="-000"
        self.ip="unknwon"
        thread.start_new_thread(self.__status,())

    def __cpu_temperature(self):
        os_popen = os.popen('/opt/vc/bin/vcgencmd measure_temp')
        res = os_popen.readline()
        os_popen.close()
        return res.replace("temp=","").replace('\n','')
    def __ip(self):
        os_popen = os.popen('ip a|grep inet|grep global')
        line = os_popen.readline()
        os_popen.close()
        return line.replace('\n','')
    def __cpu_id(self):
        os_popen = os.popen('cat /proc/cpuinfo |grep Serial')
        res = os_popen.readline()
        os_popen.close()
        return re.subn("Serial[\t]*: ","",res)[0].replace('\n','')

    def __uptime(self):
        os_popen = os.popen('uptime')
        line = os_popen.readline()
        os_popen.close()
        return line.replace('\n','')

    def __status(self):
        while True:
            try:
                self.uptime = self.__uptime()
                self.cpu_temperature = self.__cpu_temperature()
                self.ip=self.__ip()
                self.logger.info("status checked ")
                time.sleep(60)
            except Exception,e:
                self.logger.info('Some error/exception occurred %s',e)
                self.logger.error(traceback.format_exc())
