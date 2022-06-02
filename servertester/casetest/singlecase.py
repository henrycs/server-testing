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
    case1 = TestCase("601138.XSHG", 15.8, 1200, OrderSide.BUY, OrderType.MARKET)
    case1.add_first_stage(OrderStatus.ALL, 5.77, 1200, 20)
    load_case(case1)

def buy_test_case3():
    case1 = TestCase("600000.XSHG", 5.5, 3000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.PARTIAL, 5.1, 1000, 12.3)
    case1.add_stage(TestAction.UPDATE, OrderStatus.PARTIAL, 5.15, 2000, 13.45)
    case1.add_stage(TestAction.UPDATE, OrderStatus.ALL, 5.2, 3000, 15.2)
    load_case(case1)


def sell_test_case1():
    case1 = TestCase("600000.XSHG", 5.6, 1000, OrderSide.SELL, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.58, 1000, 10)
    load_case(case1)

def buy_test_case9():
    case1 = TestCase("601118.XSHG", 6.99, 2000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.CANCEL, OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.UPDATE, OrderStatus.CANCEL, 6.8, 1000, 10.23)
    load_case(case1)

def run_mem_test_cases():
    buy_test_case2()

