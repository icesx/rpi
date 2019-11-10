#!/usr/bin/python
from controller.controller import Controller
from server.communication import Communication
from entrancer.entrancer import Entrancer
from alarm.alarm import Alarm
from fence.fence import Fence
from log import logger_creater


def main():
    logger = logger_creater.init_log(__name__)
    logger.info("all-start..............")
    ctrl = Controller()
    heart_url = "http://192.168.24.250:8094/fk/Raspberry/SyncSwitch.do"
    entrancer = Entrancer(10,11)
    ctrl.control(Communication(heart_url,entrancer),
                 entrancer,
                 Alarm(12),
                 Fence(36))


if __name__ == '__main__':
    main()
