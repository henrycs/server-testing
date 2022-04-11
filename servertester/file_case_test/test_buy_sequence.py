from servertester.initialize import client, server, mock_server_proceed, mock_server_load_case, print_result

def testcase_f20_01_04():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    result = mock_server_load_case("f20-01")
    if not result:
        return None

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.76, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_load_case("f20-02")
    if not result:
        return None

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.76, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_load_case("f20-03")
    if not result:
        return None

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.76, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    result = mock_server_load_case("f20-04")
    if not result:
        return None

    input("next case: buy 600107.XSHG......")
    result = client.buy(security="600107.XSHG", price=6.76, volume=1000)
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)            