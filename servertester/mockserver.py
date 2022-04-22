# -*- coding: utf-8 -*-
import logging
from servertester.sdk.transport import get, post_json

logger = logging.getLogger(__name__)

class MockServer:
    def __init__(self, url, token, account):
        self.url = url
        self.token = token
        self.account = account
        self.headers = {"Authorization": self.token}
        self.headers["Account-ID"] = self.account

    def load(self, case: str):
        url = self.url + '/load'
        data = {"case": case}
        result = post_json(url, params=data, headers=self.headers)
        if result is None:
            logger.error("load_case: failed to get response")
            return False
        
        if result['status'] != 0:
            logger.info(result['msg'])
            return False
        else:
            logger.info(result['data'])
            return True

    def load_data(self, case: str):
        url = self.url + '/load_data'
        result = post_json(url, params=case, headers=self.headers)
        if result is None:
            logger.error("load_case: failed to get response")
            return False
        
        if result['status'] != 0:
            logger.info(result['msg'])
            return False
        else:
            logger.info(result['data'])
            return True

    def proceed(self):
        url = self.url + '/proceed'
        result = get(url, params=None, headers=self.headers)
        if result is None:
            logger.error("proceed: failed to get response")
            return {'status': -1, 'msg': 'failed to get response'}

        return result        


    def reset(self):
        url = self.url + '/reset'
        result = get(url, params=None, headers=self.headers)
        if result is None:
            logger.error("reset: failed to get response")
            return False
        
        if result['status'] != 0:
            logger.info(result['msg'])
            return False
        else:
            logger.info(result['data'])
            return True            
       