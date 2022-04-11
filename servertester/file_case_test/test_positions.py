from servertester.initialize import client, server, mock_server_proceed, mock_server_load_case, print_result


def testcase_f07_03():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600107.XSHG......")
    result = client.sell(security="600107.XSHG", price=6.76, volume=1200)
    print_result(result)




def testcase_f07_02():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.76, volume=1200)
    print_result(result)

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.80, volume=500)
    print_result(result)


def testcase_f07_03():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: sell 600107.XSHG......")
    result = client.sell(security="600107.XSHG", price=6.76, volume=1200)
    print_result(result)

