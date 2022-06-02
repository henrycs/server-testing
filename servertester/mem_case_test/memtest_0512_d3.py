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
    case1 = TestCase("600000.XSHG", 5.6, 1000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.58, 1000, 10)
    run_stages_in_case(case1)

def sell_test_case2():
    case1 = TestCase("600000.XSHG", 5.7, 2000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.67, 2000, 12)
    run_stages_in_case(case1)

def sell_test_case3():
    case1 = TestCase("600000.XSHG", 5.72, 1000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.70, 1000, 12)
    run_stages_in_case(case1)

def sell_test_case4():
    case1 = TestCase("600000.XSHG", 5.3, 2500, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 5.2, 1000, 11)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 5.11, 1800, 11.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 5.0, 2000, 15.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 4.99, 2500, 16.2)
    run_stages_in_case(case1)



def buy_test_case5():
    case1 = TestCase("000417.XSHE", 4.55, 2000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 4.49, 2000, 10)
    run_stages_in_case(case1)

def sell_test_case6():
    case1 = TestCase("601138.XSHG", 9.51, 1800, OrderSide.SELL, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 9.53, 1800, 22.2)
    run_stages_in_case(case1)
def buy_test_case6():
    case1 = TestCase("601138.XSHG", 9.45, 1900, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.PARTIAL, 9.43, 1000, 12.3)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 9.41, 1200, 13.45)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 9.37, 1900, 15.2)
    run_stages_in_case(case1)

def sell_test_case7():
    case1 = TestCase("601118.XSHG", 6.81, 1000, OrderSide.SELL, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 6.99, 1000, 22.2)
    run_stages_in_case(case1)
def buy_test_case7():
    case1 = TestCase("601118.XSHG", 6.95, 1400, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.CANCEL, OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.UPDATE, OrderStatus.CANCEL, 6.87, 1100, 16.23)
    run_stages_in_case(case1)



def buy_test_case22():
    case1 = TestCase("600519.XSHG", 1828.38, 200, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 1823.0, 200, 2330.1)
    run_stages_in_case(case1)

def sell_test_case21():
    case1 = TestCase("601118.XSHG", 6.6, 1000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 6.58, 1000, 10)
    run_stages_in_case(case1)

def buy_test_case21():
    case1 = TestCase("600519.XSHG", 1828.38, 300, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 1828.0, 300, 1330.1)
    run_stages_in_case(case1)


def run_mem_test_cases(stage=1):
    print("------------- info --------------")
    result = client.basic_info()
    print_result(result)

    if stage == 1:
        sell_test_case1()
        buy_test_case1()
        sell_test_case2()
        buy_test_case2()
        sell_test_case3()
        buy_test_case3()
        sell_test_case4()
        buy_test_case4()

        buy_test_case5()
        sell_test_case6()
        buy_test_case6()
        sell_test_case7()
        buy_test_case7()

        buy_test_case22()
    elif stage == 2:    
        sell_test_case21()
    else:
        buy_test_case21()
