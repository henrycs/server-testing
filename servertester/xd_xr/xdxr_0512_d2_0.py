from servertester.generators.TestCase import TestCase
from servertester.generators.entrusts import TestAction
from servertester.initialize import print_result
from servertester.sdk.trade import OrderSide, OrderStatus, OrderType
from servertester.generators.executor import run_stages_in_case
from servertester.initialize import client



def sell_test_case1():
    case1 = TestCase("002465.XSHE", 5.72, 100, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    run_stages_in_case(case1)

def sell_test_case2():
    case1 = TestCase("300037.XSHE", 5.72, 200, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    run_stages_in_case(case1)

def sell_test_case3():
    case1 = TestCase("600000.XSHG", 5.6, 500, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    run_stages_in_case(case1)


def run_mem_test_cases(stage=1):
    print("------------- info --------------")
    result = client.basic_info()
    print_result(result)

    sell_test_case1()
    sell_test_case2()    
    sell_test_case3()
