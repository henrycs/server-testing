from servertester.initialize import client, server, mock_server_proceed, mock_server_load_case, print_result



def testcase_f40_01_04():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    result = mock_server_load_case("f40-01")
    if not result:
        return None

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.2, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_load_case("f40-02")
    if not result:
        return None

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.2, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_load_case("f40-03")
    if not result:
        return None

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.2, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_load_case("f40-04")
    if not result:
        return None

    input("next case: sell 600000.XSHG......")
    result = client.sell(security="600000.XSHG", price=5.2, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)
    

def testcase_f40_11_14():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    result = mock_server_load_case("f40-11")
    if not result:
        return None

    input("next case: sell 600107.XSHG......")
    result = client.sell(security="600107.XSHG", price=6.76, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_load_case("f40-12")
    if not result:
        return None

    input("next case: sell 600107.XSHG......")
    result = client.sell(security="600107.XSHG", price=6.76, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_load_case("f40-13")
    if not result:
        return None

    input("next case: sell 600107.XSHG......")
    result = client.sell(security="600107.XSHG", price=6.76, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_load_case("f40-14")
    if not result:
        return None

    input("next case: sell 600107.XSHG......")
    result = client.sell(security="600107.XSHG", price=6.76, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)            