# Copyright (C)
# Author: I
# Contact: 12157724@qq.com

import json
from transform_object import ReciveInfo
from distutils.util import strtobool
OPEN_ONCE = "is_open_once"

CLOSE = "close"

OPEN_LONG = "is_open_long"


def recive_decoder(json):
    return ReciveInfo(strtobool(json[OPEN_ONCE]),strtobool(json[OPEN_LONG]),strtobool(json[CLOSE]))

def default_decorder():
    return ReciveInfo(False,False,False)

def report_encoder(report):
    return json.dumps(report.__dict__)
