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
    case1 = TestCase("601118.XSHG", 6.99, 2000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.CANCEL, OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.UPDATE, OrderStatus.CANCEL, 6.8, 1000, 10.23)
    run_stages_in_case(case1)

def buy_test_case4():
    case1 = TestCase("000882.XSHE", 1.86, 5000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 1.8, 3000, 12.3)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 1.85, 5000, 15.2)
    run_stages_in_case(case1)

def buy_test_case5():
    case1 = TestCase("603133.XSHG", 8.8, 2000, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ERROR, 0, 0, 0)
    run_stages_in_case(case1)

def buy_test_case6():
    case1 = TestCase("600000.XSHG", 5.8, 1200, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    run_stages_in_case(case1)

def buy_test_case7():
    case1 = TestCase("600000.XSHG", 5.9, 1300, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    run_stages_in_case(case1)




def sell_test_case1():
    case1 = TestCase("600000.XSHG", 5.9, 1300, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    run_stages_in_case(case1)

def sell_test_case2():
    case1 = TestCase("601118.XSHG", 6.9, 500, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 7.0, 500, 10)
    run_stages_in_case(case1)
def sell_test_case3():
    case1 = TestCase("601118.XSHG", 6.9, 500, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 7.2, 500, 12)
    run_stages_in_case(case1)

def sell_test_case4():
    case1 = TestCase("600000.XSHG", 5.1, 3700, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 5.0, 1000, 11)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 4.99, 1700, 11.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 4.9, 2700, 15.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 4.88, 3700, 16.2)
    run_stages_in_case(case1)

def sell_test_case5():
    case1 = TestCase("000882.XSHE", 1.85, 4000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 1.87, 1000, 11)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 1.9, 2000, 11.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 1.92, 3000, 15.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 1.95, 4000, 16.2)
    run_stages_in_case(case1)


def sell_test_case6():
    case1 = TestCase("600000.XSHG", 5.2, 2000, OrderSide.SELL, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 5.5, 2000, 66)
    run_stages_in_case(case1)
def sell_test_case7():
    case1 = TestCase("000882.XSHE", 1.83, 1000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 1.83, 1000, 11.2)
    run_stages_in_case(case1)

def run_mem_test_cases():
    print("------------- info --------------")
    result = client.basic_info()
    print_result(result)

    #sell_test_case1()
    #sell_test_case2()
    #sell_test_case3()
    #sell_test_case4()
    #sell_test_case5()
    #sell_test_case6()
    #sell_test_case7()

    buy_test_case6()
    buy_test_case1()