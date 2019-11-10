# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

"""
the reporter json format is
{
time:"2018-02-33 06:08:04",
event:"warn|heart"
state:"opend|closed"
id:"00000000b09e6c08"
ip:"192.168.1.4"
temperature:"58.5'c"
uptime:"21:01:03 up 12:44,  1 user,  load average: 0.00, 0.00, 0.00"
}
"""


class ReportInfo(object):
    WARN = 'warn'
    HEART = "heart"

    def __init__(self,time,event,entencer_state,hw_status):
        self.time = time
        self.event = event
        self.id = hw_status.id
        self.ip = hw_status.ip
        self.temperature = hw_status.cpu_temperature
        self.uptime = hw_status.uptime
        self.state = entencer_state


"""
report some event to server

the command json format is
{
is_open_once="True|False",
is_open_long="True|False",
close="true|false"
}


"""


class ReciveInfo(object):
    def __init__(self,is_open_once,is_open_long,close):
        self.is_open_once = is_open_once
        self.is_open_long = is_open_long
        self.close = close

    def __str__(self):
        return "open_long=%s,open_once=%s,close=%s" % (self.is_open_long,self.is_open_once,self.close)
