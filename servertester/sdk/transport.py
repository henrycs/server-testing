import uuid
import requests
import cfg4py
import logging



logger = logging.getLogger(__name__)



def status_ok(code: int):
    return code in [200, 201, 204]

class TradeError(Exception):
    """交易中的异常

    当捕获异常后，可以通过status_code和message属性来获取错误代码和详细错误信息。
    """

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def __str__(self):
        return f"{self.message}: {self.args}"


def process_response_result(rsp):
    content_type = rsp.headers.get("Content-Type")

    # process 20x response, check response code first
    if status_ok(rsp.status_code):
        if content_type == "application/json":
            return rsp.json()
        elif content_type.startswith("text"):
            return rsp.text
        else:
            return pickle.loads(rsp.content)

    # http 1.1 allow us to extend http status code, so we choose 499 as our error code.
    # The upstream server is currently built on top of sanic,
    # it doesn't support customer reason phrase (always return "Unknown Error" if the status code is extened.
    # So we have to use body to carry on reason phrase.
    if rsp.status_code == 499:
        logger.warning("trade action failed: %s, %s", rsp.status_code, rsp.text)
        raise TradeError(rsp.status_code, rsp.text)
    else:
        rsp.raise_for_status()


def get(url, params=None, headers=None):
    if headers is None:
        headers = {"Request-ID": uuid.uuid4().hex}
    else:
        headers.update({"Request-ID": uuid.uuid4().hex})

    rsp = requests.get(url, params=params, headers=headers)
    result = process_response_result(rsp)

    return result


def post_json(url, params=None, headers=None):
    if headers is None:
        headers = {"Request-ID": uuid.uuid4().hex}
    else:
        headers.update({"Request-ID": uuid.uuid4().hex})

    rsp = requests.post(url, json=params, headers=headers)
    return process_response_result(rsp)

