# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
class WeigendData:
    def __init__(self,bits):
        print "bits length",len(bits),"".join(str(x) for x in bits)
        if len(bits) == 26:
            self.card = "".join(str(x) for x in bits[1:25])
        else:
            self.card = "".join(str(x) for x in bits)

    def get_cardno(self):
        return int(self.card,2)
