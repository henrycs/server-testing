from servertester.initialize import client, server, mock_server_proceed, mock_server_load_case, print_result


def testcase_f06_01():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 003023.XSHE......")
    result = client.buy(security="003023.XSHE", price=24.4, volume=600)
    print_result(result)

    input("next case: cancel_entrust 5acd03f0-544c-4e17-8db4-a9a08bf69eb6 ......")
    result = client.cancel_entrust("5acd03f0-544c-4e17-8db4-a9a08bf69eb6")
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)


def testcase_f06_02():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 003023.XSHE......")
    result = client.buy(security="003023.XSHE", price=24.4, volume=600)
    print_result(result)

    input("next case: buy 000001.XSHE ......")
    result = client.buy(security="000001.XSHE", price=4.2, volume=1200)
    print_result(result)

    input("next case: cancel_all_entrust ......")
    result = client.cancel_all_entrusts()
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)


def testcase_f06_03():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 003023.XSHE......")
    result = client.buy(security="003023.XSHE", price=24.4, volume=600)
    print_result(result)

    input("next case: cancel_entrust ba0a8ee8-a9c6-4c52-abb7-c5bdcbe20241 ......")
    result = client.cancel_entrust("ba0a8ee8-a9c6-4c52-abb7-c5bdcbe20241")
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)
