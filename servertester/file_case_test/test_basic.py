from servertester.initialize import client, print_result

def testcase_f01_01():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: today_entrusts ......")
    result = client.today_entrusts()
    print_result(result)

    input("next case: positions ......")
    result = client.positions()
    print_result(result)

    input("next case: balance ......")
    result = client.balance()
    print_result(result)

    input("next case: available_money ......")
    result = client.available_money()
    print_result(result)


def testcase_f01_02():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 600000.XSH......")
    result = client.buy(security="600000.XSHG", price=6.99, volume=1800)
    print_result(result)

    input("next case: positions ......")
    result = client.positions()
    print_result(result)

    print("------------- info --------------")
    result = client.info()
    print_result(result)


def testcase_f01_03():
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    input("next case: buy 000020.XSHE......")
    result = client.buy(security="000020.XSHE", price=99.94, volume=100)
    print_result(result)

    input("next case: buy 001030.XSHE......")
    result = client.buy(security="001030.XSHE", price=9.94, volume=100)
    print_result(result)

    input("next case: positions ......")
    result = client.positions()
    print_result(result)

    input("next case: balance ......")
    result = client.balance()
    print_result(result)

    print("------------- info --------------")
    result = client.info()
    print_result(result)
