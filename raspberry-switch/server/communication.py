import traceback

import requests

from server import json_coder
from server.transform_object import ReportInfo
import datetime
import thread
import time

from log import logger_creater
import json
from status.status import PiStatus


class Communication:
    headers = {
        "Content-Type": "application/json"
    }

    def __init__(self,heat_beat_url,entrancer):
        self.heat_beat_url = heat_beat_url
        self.logger = logger_creater.init_log(__name__)
        self.reciverInfo = json_coder.default_decorder()
        self.entrancer = entrancer
        self.status = PiStatus()
        if heat_beat_url is not None:
            thread.start_new_thread(self.__heat_beat,())

    def warn(self):
        self.__report(ReportInfo.WARN)

    def __report(self,action):
        report = ReportInfo(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),action,self.entrancer.state,
                            self.status)
        report_json = json_coder.report_encoder(report)
        self.logger.info("report json is %s",report_json)
        respose = requests.post(self.heat_beat_url,data=report_json,headers=self.headers,timeout=5)
        self.logger.info("receive json is %s",respose.text)
        if respose.text:
            json_=respose.json()
            self.reciverInfo = json_coder.recive_decoder(json.loads(json_))
        else:
            self.logger.error("receive empty from server")
            self.reciverInfo = json_coder.default_decorder()

    def heat_beat(self):
        return self.reciverInfo

    def __heat_beat(self):
        while True:
            try:
                self.__report(ReportInfo.HEART)
            except Exception,e:
                self.logger.error(traceback.format_exc())
                self.reciverInfo = json_coder.default_decorder()
            time.sleep(1)
