from servertester.initialize import client, server, mock_server_proceed, mock_server_load_case, print_result

def testcase_f02_01():
    result = mock_server_load_case("f02-01")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 600000.XSHG......")
    result = client.buy(security="600000.XSHG", price=6.99, volume=2100)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)


def testcase_f02_02():
    result = mock_server_load_case("f02-02")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 600009.XSHG......")
    result = client.buy(security="600009.XSHG", price=6.99, volume=2100)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None    

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None    


def testcase_f02_03():
    result = mock_server_load_case("f02-03")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 601118.XSHG......")
    result = client.buy(security="601118.XSHG", price=6.99, volume=2100)
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None    

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    input("next case: cancel_all_entrust ......94c40593-9eb5-44cd-85fc-6ea1e19ce55a")
    result = client.cancel_entrust(cid="94c40593-9eb5-44cd-85fc-6ea1e19ce55a")
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None    

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)


def testcase_f02_04():
    result = mock_server_load_case("f02-04")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.76, volume=1200)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

def testcase_f02_14():
    result = mock_server_load_case("f02-14")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.76, volume=1600)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

def testcase_f02_30():
    result = mock_server_load_case("f02-30")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 003023.XSHE......")
    result = client.buy(security="003023.XSHE", price=24.4, volume=600)
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)


def testcase_f02_31():
    result = mock_server_load_case("f02-31")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.76, volume=150000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)


def testcase_f02_32():
    result = mock_server_load_case("f02-32")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.76, volume=1200)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)


def testcase_f03_01():
    result = mock_server_load_case("f03-01")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: market buy 600000.XSHG......")
    result = client.market_buy(security="600000.XSHG", price=5.20, volume=10000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

def testcase_f03_02():
    result = mock_server_load_case("f03-02")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: market buy 600000.XSHG......")
    result = client.market_buy(security="600000.XSHG", price=5.20, volume=2000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_proceed()
    if not result:
        return None

def testcase_f03_03():
    result = mock_server_load_case("f03-03")
    if not result:
        return None

    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: market buy 600000.XSHG......")
    result = client.market_buy(security="600000.XSHG", price=5.20, volume=10000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)