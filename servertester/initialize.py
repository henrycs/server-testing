import logging
from mockserver import MockServer
from servertester.sdk.client import TradeClient


logger = logging.getLogger(__name__)


# init Trade Client
url = "http://192.168.100.202:8000/api/trade/v0.1"
acct = "henry"
token = "f1a055f7-cba3-42fc-89e7-791c97603eaa"
client = TradeClient(url, acct, token)

# init Mock server controller
server_url = "http://192.168.100.202:9001/mock"
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

def mock_server_load_case_data(case: str, clear=True):
    if clear:
        result = server.reset()
        if not result:
            return False

    print(f"load case {case} ......")
    result = server.load(case)
    return result

def mock_server_proceed(caseid):
    input("proceed to next stage in test case, press any key ......")
    result = server.proceed(caseid)
    return result

def print_result(result):
    if result is None:
        logger.error("failed to get information")
        return None

    print("response: \n")
    if isinstance(result, list):
        for data in result:
            print(f"{data}\n")
    else:
        print(f"{result}\n")

    print("\n")
