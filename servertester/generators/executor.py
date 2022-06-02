import os
from servertester.initialize import client, mock_server_load_case_data, mock_server_proceed, print_result
from servertester.generators.entrusts import Entrust, StageInfo, TestAction, get_action
from servertester.generators.TestCase import TestCase


def run_stage(action: TestAction, entrust: Entrust, stage: StageInfo, caseid: str):
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
        result = mock_server_proceed(caseid)
    
    print_result(result)
    if result is None:
        return False
    else:
        return True


def run_stages_in_case(case: TestCase):
    print("------------- info --------------")
    result = client.basic_info()
    print_result(result)

    # get all actions from test case
    entrust: Entrust = case.entrust
    stage_list: list = case.stages

    result = mock_server_load_case_data(case.toDict())
    if not result:
        return None
    # {'case': '41e935851df14343a2e905770e8b69b3', 'stage': 'stage1', 'action': 'buy', 'status': 'to be executed'}
    caseid = result['case']

    for stage in stage_list:
        action = stage.test_action
        print(f"stage: {stage.stage_name}, action: {get_action(action)}")
        result = run_stage(action, entrust, stage, caseid)
        if result is False:
            print("error occured, exit....")
            os._exit(1)

        input("next case: today_entrusts ......")
        result = client.today_entrusts()
        print_result(result)