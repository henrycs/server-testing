from servertester.generators.TestCase import TestCase
from servertester.generators.entrusts import TestAction
from servertester.initialize import print_result
from servertester.sdk.trade import OrderSide, OrderStatus, OrderType
from servertester.generators.executor import run_stages_in_case
from servertester.initialize import client


   
def buy_test_case1():
    case1 = TestCase("600000.XSHG", 5.2, 1000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.16, 1000, 11.22)
    run_stages_in_case(case1)

def buy_test_case2():
    case1 = TestCase("600000.XSHG", 5.5, 3000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 5.1, 1000, 12.3)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 5.15, 2000, 13.45)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 5.2, 3000, 15.2)
    run_stages_in_case(case1)

def buy_test_case3():
    case1 = TestCase("600000.XSHG", 5.8, 1200, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 5.77, 1200, 20)
    run_stages_in_case(case1)

def buy_test_case4():
    case1 = TestCase("600000.XSHG", 5.9, 1300, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.8, 1300, 12)
    run_stages_in_case(case1)

def sell_test_case1():
    case1 = TestCase("600000.XSHG", 5.6, 500, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.59, 500, 10)
    run_stages_in_case(case1)

def sell_test_case2():
    case1 = TestCase("600000.XSHG", 5.7, 700, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.69, 700, 12)
    run_stages_in_case(case1)

def sell_test_case3():
    case1 = TestCase("600000.XSHG", 5.72, 800, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.71, 800, 12)
    run_stages_in_case(case1)

def sell_test_case4():
    case1 = TestCase("600000.XSHG", 5.1, 2000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 5.0, 800, 11)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 4.99, 1500, 11.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 4.88, 2000, 16.2)
    run_stages_in_case(case1)



def sell_test_case5():
    case1 = TestCase("300037.XSHE", 39.5, 1300, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 39.56, 1300, 10)
    run_stages_in_case(case1)

def sell_test_case6():
    case1 = TestCase("002465.XSHE", 9.15, 900, OrderSide.SELL, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 9.15, 900, 22.2)
    run_stages_in_case(case1)

def buy_test_case5():
    case1 = TestCase("002465.XSHE", 9.18, 1800, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.PARTIAL, 9.17, 1000, 12.3)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 9.16, 1200, 13.45)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 9.16, 1800, 15.2)
    run_stages_in_case(case1)

def buy_test_case6():
    case1 = TestCase("600989.XSHG", 14.03, 1600, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 14.02, 1600, 15.2)
    run_stages_in_case(case1)

def sell_test_case7():
    case1 = TestCase("603078.XSHG", 24.51, 3000, OrderSide.SELL, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 24.55, 3000, 22.2)
    run_stages_in_case(case1)

def buy_test_case7():
    case1 = TestCase("603078.XSHG", 24.6, 1800, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.PARTIAL, 24.6, 1000, 12.3)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 24.55, 1200, 13.45)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 24.5, 1800, 15.2)
    run_stages_in_case(case1)


def run_mem_test_cases(stage=1):
    print("------------- info --------------")
    result = client.basic_info()
    print_result(result)

    sell_test_case1()
    buy_test_case1()
    sell_test_case2()
    buy_test_case2()
    sell_test_case3()
    buy_test_case3()
    sell_test_case4()
    buy_test_case4()

    sell_test_case5()
    sell_test_case6()
    buy_test_case5()
    buy_test_case6()
    sell_test_case7()
    buy_test_case7()
