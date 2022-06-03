from servertester.generators.TestCase import TestCase
from servertester.generators.entrusts import TestAction
from servertester.initialize import print_result
from servertester.sdk.trade import OrderSide, OrderStatus, OrderType
from servertester.generators.executor import run_stages_in_case
from servertester.initialize import client

   
def buy_test_case1():
    case1 = TestCase("301073.XSHE", 45.2, 1000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 45.1, 1000, 43.22)
    run_stages_in_case(case1)

def buy_test_case2():
    case1 = TestCase("002443.XSHE", 8.1, 3000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 8.1, 1000, 12.3)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 8.05, 2000, 13.45)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 8.0, 3000, 15.2)
    run_stages_in_case(case1)

def buy_test_case3():
    case1 = TestCase("601156.XSHG", 23.6, 1200, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 23.5, 1200, 20)
    run_stages_in_case(case1)

def buy_test_case4():
    case1 = TestCase("000803.XSHE", 13.1, 1300, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 13.1, 1300, 21)
    run_stages_in_case(case1)

def buy_test_case5():
    case1 = TestCase("600000.XSHG", 7.8, 4000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 7.8, 4000, 18.7)
    run_stages_in_case(case1)


def run_mem_test_cases(stage=1):
    print("------------- info --------------")
    result = client.basic_info()
    print_result(result)

    buy_test_case1()
    buy_test_case2()
    buy_test_case3()
    buy_test_case4()
    buy_test_case5()
