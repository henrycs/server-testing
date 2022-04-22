from servertester.initialize import client, mock_server_load_case_data, mock_server_proceed, print_result
from servertester.generators.entrusts import Entrust, StageInfo, TestAction, get_action
from servertester.generators.TestCase import TestCase


def run_stage(action: TestAction, entrust: Entrust, stage: StageInfo):
    action_name = get_action(action)

    if action == TestAction.BUY:
        input(f"next case: {action_name}, {entrust.code}, {entrust.price}, {entrust.volume}")
        result = client.buy(security=entrust.code, price=entrust.price, volume=entrust.volume)
    elif action == TestAction.MARKET_BUY:
        input(f"next case: {action_name}, {entrust.code}, {entrust.price}, {entrust.volume}")
        result = client.market_buy(security=entrust.code, volume=entrust.volume)
    elif action == TestAction.SELL:
        input(f"next case: {action_name}, {entrust.code}, {entrust.price}, {entrust.volume}")
        result = client.sell(security=entrust.code, price=entrust.price, volume=entrust.volume)
    elif action == TestAction.MARKET_SELL:
        input(f"next case: {action_name}, {entrust.code}, {entrust.price}, {entrust.volume}")
        result = client.market_sell(security=entrust.code, volume=entrust.volume)
    elif action == TestAction.CANCEL:
        input(f"next case: {action_name}, {entrust.entrust_no}")
        result = client.cancel_entrust(cid=entrust.entrust_no)
    else:
        result = mock_server_proceed()

    print_result(result)



def run_stages_in_case(case: TestCase):
    print("------------- info --------------")
    result = client.info()
    print_result(result)

    # get all actions from test case
    entrust: Entrust = case.entrust
    stage_list: list = case.stages

    result = mock_server_load_case_data(case.toDict())
    if not result:
        return None

    for stage in stage_list:
        action = stage.test_action
        print(f"stage: {stage.stage_name}, action: {get_action(action)}")
        run_stage(action, entrust, stage)

        input("next case: today_entrusts ......")
        result = client.today_entrusts()
        print_result(result)