# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import logging
import logging.handlers

formatter = logging.Formatter(
    fmt='%(asctime)s - [%(levelname)s] - [%(threadName)s] - [%(filename)s:%(lineno)s] - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)


def init_log(name="",file="/home/pi/logs/raspberry-swith.log"):
    rf_handler = logging.handlers.TimedRotatingFileHandler(file,when='MIDNIGHT',interval=1,backupCount=7)
    rf_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(rf_handler)
    logger.addHandler(ch)
    print "===========> create logging<==========="
    return logger

