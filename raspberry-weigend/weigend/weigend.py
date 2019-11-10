# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import time
import thread
from weigend_data import WeigendData


class weigend:
    def __init__(self,callback):
        self.bits = []
        self.current_time = 0l
        self.callback = callback
        thread.start_new_thread(self._check_timeout,())

    def set_bit(self,bit):
        self.current_time = self.__current()
        self.bits.append(bit)

    def __current(self):
        return long(time.time() * 1000)

    def _check_timeout(self):
        print "check thread started..."
        while (True):
            # print self.current_time,self.__current()
            if self.current_time + 5 < self.__current():
                if len(self.bits) > 0:
                    print "fire callback"
                    self.callback(WeigendData(self.bits))
                    self.bits = []
                    self.current_time = self.__current();
            time.sleep(0.1)
