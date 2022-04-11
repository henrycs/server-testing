from servertester.generators.TestCase import TestCase
from servertester.generators.entrusts import OrderSide, OrderStatus, TestAction
from servertester.generators.executor import run_stages_in_case


def run_test_case():
    case1 = TestCase("601118.XSHG", 6.99, 2000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.CANCEL, OrderStatus.NO_DEAL, 0, 0, 0)
    case1.add_stage(TestAction.UPDATE, OrderStatus.CANCEL, 7.0, 1000, 10.23)
    #print(case1.toDict())
    run_stages_in_case(case1)
    
def run_test_case2():
    case1 = TestCase("600000.XSHG", 5.2, 1000, OrderSide.BUY, OrderType.LIMIT)
    case1.add_first_stage(OrderStatus.ALL, 5.1, 1000, 11.22)
    run_stages_in_case(case1)



def run_mem_test_cases():
    run_test_case()