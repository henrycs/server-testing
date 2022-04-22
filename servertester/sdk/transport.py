import uuid
import requests
import cfg4py
import logging



logger = logging.getLogger(__name__)



def status_ok(code: int):
    return code in [200, 201, 204]


def process_response_result(rsp):
    content_type = rsp.headers.get("Content-Type")

    try:
        # process 20x response, check response code first
        if status_ok(rsp.status_code):
            if content_type == "application/json":
                json_data = rsp.json()
                # 返回值必须符合文档的定义
                if "status" in json_data and "msg" in json_data:
                    return json_data
                else:
                    logger.error("invalid json response: %s", json_data)

            # invalid response from trade server
            if content_type.startswith("text"):
                logger.error("invalid text response, %s", rsp.text)
            else:
                logger.error("invalid response, %s", rsp.raw)

        # process errros, response code as 40x, 50x
        else:
            if content_type == "application/json":
                result = rsp.json()
                logger.error(
                    "exec failed, response code: %d, msg: %s",
                    rsp.status_code,
                    result,
                )
            else:  # just save content to log file
                logger.error(
                    "exec failed: response code: %d, extra msg: %s",
                    rsp.status_code,
                    rsp.reason,
                )

    except Exception as e:
        logger.exception(e)

    return None


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



