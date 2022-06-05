from servertester.generators.TestCase import TestCase
from servertester.generators.entrusts import Entrust, TestAction
from servertester.initialize import mock_server_load_case_data, print_result
from servertester.sdk.trade import OrderSide, OrderStatus, OrderType
from servertester.generators.executor import run_stages_in_case
from servertester.initialize import client



def load_case(case):
    # get all actions from test case
    entrust: Entrust = case.entrust
    stage_list: list = case.stages

    result = mock_server_load_case_data(case.toDict(), False)
    if not result:
        return None

   
def buy_test_case1():
    case1 = TestCase("600000.XSHG", 15.2, 1000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.16, 1000, 11.22)
    load_case(case1)

def buy_test_case2():
    case1 = TestCase("601138.XSHG", 15.8, 200, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 5.77, 200, 20)
    load_case(case1)

def buy_test_case3():
    case1 = TestCase("601118.XSHG", 6.99, 300, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.CANCEL, OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.UPDATE, OrderStatus.CANCEL, 6.77, 100, 6.23)
    load_case(case1)


def sell_test_case1():
    case1 = TestCase("000417.XSHE", 5.6, 2000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.58, 2000, 10)
    load_case(case1)

def sell_test_case2():
    case1 = TestCase("601118.XSHG", 5.6, 200, OrderSide.SELL, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 5.58, 200, 10)
    load_case(case1)


def run_mem_test_cases(stage=1):
    buy_test_case3()

