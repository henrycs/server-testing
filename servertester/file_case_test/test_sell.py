from servertester.initialize import client, server, mock_server_proceed, mock_server_load_case, print_result

def testcase_f04_01():
    result = mock_server_load_case("f04-01")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.20, volume=100)
    print_result(result)

def testcase_f04_02():
    result = mock_server_load_case("f04-02")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.20, volume=12000)
    print_result(result)

def testcase_f04_03():
    result = mock_server_load_case("f04-03")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.20, volume=10000)
    print_result(result)

def testcase_f04_05():
    result = mock_server_load_case("f04-05")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.20, volume=1000)
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None

def testcase_f04_06():
    result = mock_server_load_case("f04-06")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.20, volume=1000)
    print_result(result)

    input("next case: cancel_all_entrust ......89ebbc20-2ee8-4a76-86c4-96a52268a40c")
    result = client.cancel_entrust(cid="89ebbc20-2ee8-4a76-86c4-96a52268a40c")
    print_result(result)


def testcase_f04_07():
    result = mock_server_load_case("f04-07")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.20, volume=1000)
    print_result(result)

    input("next case: cancel_all_entrust ......14ea0c05-deec-4a00-af15-20733c103a80")
    result = client.cancel_entrust(cid="14ea0c05-deec-4a00-af15-20733c103a80")
    print_result(result)

def testcase_f04_08():
    result = mock_server_load_case("f04-08")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.20, volume=100)
    print_result(result)


def testcase_f04_09():
    result = mock_server_load_case("f04-09")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.20, volume=600)
    print_result(result)

def testcase_f04_10():
    result = mock_server_load_case("f04-10")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600107.XSHG......")
    result = client.sell(security="600107.XSHG", price=6.6, volume=2800)
    print_result(result)


def testcase_f05_01():
    result = mock_server_load_case("f05-01")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: market sell 600000.XSHG......")
    result = client.market_sell(security="600000.XSHG", price=5.20, volume=9000)
    print_result(result)

def testcase_f05_02():
    result = mock_server_load_case("f05-02")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.market_sell(security="600000.XSHG", price=5.20, volume=12000)
    print_result(result)


def testcase_f05_03():
    result = mock_server_load_case("f05-03")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.market_sell(security="600000.XSHG", price=5.20, volume=1000)
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None

def testcase_f05_04():
    result = mock_server_load_case("f05-04")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600000.XSHG......")
    result = client.market_sell(security="600000.XSHG", price=5.60, volume=1000)
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None