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



def sell_test_case2():
    case1 = TestCase("601118.XSHG", 6.9, 500, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 7.0, 500, 10)
    run_stages_in_case(case1)
def sell_test_case3():
    case1 = TestCase("601118.XSHG", 6.9, 500, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 7.2, 500, 12)
    run_stages_in_case(case1)

def sell_test_case4():
    case1 = TestCase("600000.XSHG", 5.1, 7000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 5.0, 2000, 11)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 4.99, 4000, 11.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 4.9, 5000, 15.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 4.88, 7000, 16.2)
    run_stages_in_case(case1)

def sell_test_case5():
    case1 = TestCase("000882.XSHE", 1.85, 5000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 1.87, 1000, 11)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 1.9, 2000, 11.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 1.92, 3000, 15.2)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 1.95, 5000, 16.2)
    run_stages_in_case(case1)




def run_mem_test_cases():
    print("------------- info --------------")
    result = client.basic_info()
    print_result(result)

    sell_test_case2()
    sell_test_case3()
    sell_test_case4()
    sell_test_case5()

    buy_test_case1()
    buy_test_case2()
    buy_test_case3()
    buy_test_case4()            