import logging
from mockserver import MockServer
from servertester.sdk.client import TradeClient


logger = logging.getLogger(__name__)


# init Trade Client
url = "http://192.168.1.201:8000/api/trade/v0.1"
acct = "henry"
token = "a2afa0ad-060c-46a6-bcb1-b1b207b71de7"
client = TradeClient(url, acct, token)

# init Mock server controller
server_url = "http://192.168.1.201:9001/mock"
server_acct = 'mockserver'
server_token = 'ec31c154fc0cbf4ba39eb48689ebcbfaacf8067f'
server = MockServer(server_url, server_token, server_acct)


def mock_server_load_case(case: str):
    result = server.reset()
    if not result:
        return False

    print(f"load case {case} ......")
    result = server.load(case)
    return result

def mock_server_load_case_data(case: str):
    result = server.reset()
    if not result:
        return False

    print(f"load case {case} ......")
    result = server.load_data(case)
    return result

def mock_server_proceed():
    input("proceed to next stage in test case, press any key ......")
    result = server.proceed()
    return result

def print_result(result):
    if result is None:
        logger.error("failed to get information")
        return None

    if result["status"] != 0:
        print(f">>>>>>>> {result['msg']}")
        return None

    print("response: \n")
    if "data" in result:
        datalist = result["data"]
        if isinstance(datalist, list):
            for data in datalist:
                print(f"{data}\n")
        else:
            print(f"{datalist}\n")
    else:
        print("no data in response")

    print("\n")
