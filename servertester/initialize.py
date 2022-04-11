import logging
from traderclient import *
from mockserver import MockServer


logger = logging.getLogger(__name__)


# init Trade Client
url = "http://192.168.100.130:8000/api/trade/v0.1"
acct = "myquant_sim_henry1"
token = "f59e34e1-71bc-46b8-8935-c60a636b9bba"
client = TradeClient(url, acct, token)

# init Mock server controller
server_url = "http://192.168.100.130:9001/mock"
server_acct = '145be423-a021-11ec-8e33-00163e0a4100'
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
