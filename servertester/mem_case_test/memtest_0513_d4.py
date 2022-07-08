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


def sell_test_case1():
    case1 = TestCase("600000.XSHG", 5.6, 1500, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.58, 1500, 10)
    run_stages_in_case(case1)

def sell_test_case2():
    case1 = TestCase("600000.XSHG", 5.72, 1000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.70, 1000, 12)
    run_stages_in_case(case1)

def sell_test_case3():
    case1 = TestCase("600519.XSHG", 1900.3, 200, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 1901, 100, 121)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 1902, 200, 126.2)
    run_stages_in_case(case1)


def buy_test_case2():
    case1 = TestCase("601138.XSHG", 9.45, 1900, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.PARTIAL, 9.43, 1000, 12.3)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 9.41, 1200, 13.45)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 9.37, 1900, 15.2)
    run_stages_in_case(case1)

def sell_test_case4():
    case1 = TestCase("601118.XSHG", 6.81, 1000, OrderSide.SELL, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 6.99, 1000, 22.2)
    run_stages_in_case(case1)


def run_mem_test_cases(stage=1):
    print("------------- info --------------")
    result = client.basic_info()
    print_result(result)

    buy_test_case1()
    sell_test_case1()    
    sell_test_case2()
    sell_test_case3()
    buy_test_case2()
    sell_test_case4()

