from servertester.generators.TestCase import TestCase
from servertester.generators.entrusts import TestAction
from servertester.initialize import print_result
from servertester.sdk.trade import OrderSide, OrderStatus, OrderType
from servertester.generators.executor import run_stages_in_case
from servertester.initialize import client

   
def buy_test_case1():  # 10派1.5元(含税)
    case1 = TestCase("002465.XSHE", 9.2, 1200, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 9.18, 1200, 43.22)
    run_stages_in_case(case1)


def buy_test_case2():  # 10派1.9元(含税)
    case1 = TestCase("600888.XSHG", 9.2, 1000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 9.18, 1000, 43.22)
    run_stages_in_case(case1)

def buy_test_case3():  #限售股股东10派2.648元，流通股股东10派3.21元
    case1 = TestCase("600989.XSHG", 14.5, 1200, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 14.48, 1200, 20)
    run_stages_in_case(case1)


def buy_test_case4():  # 10转增3股派0.9元(含税)
    case1 = TestCase("603078.XSHG", 31.7, 3000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 31.7, 1000, 12.3)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 31.65, 2000, 13.45)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 31.6, 3000, 15.2)
    run_stages_in_case(case1)

def buy_test_case5():  # 10转增8股派6.8元(含税)
    case1 = TestCase("300037.XSHE", 72.5, 1600, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 72.4, 1600, 21)
    run_stages_in_case(case1)

def buy_test_case6():
    case1 = TestCase("600000.XSHG", 7.8, 4700, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 7.8, 4700, 18.7)
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
    buy_test_case6()
