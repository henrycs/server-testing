from servertester.generators import Entrust, StageInfo, TestAction

class TestCase:
    entrust: Entrust
    stages: list

    def __init__(self, code, price, volume, order_side, order_type):
        self.entrust = Entrust(code, price, volume, order_side, order_type)
        self.stages = []

    def add_first_stage(self, status, price, filled, fees):
        idx = len(self.stages) + 1
        if idx != 1:
            print("trade action must be the first stage")
            return False

        stage1 = StageInfo(f"stage{idx}")
        stage1.set_trade_action(self.entrust.order_side, self.entrust.order_type)
        stage1.set_trade_parameters(self.entrust)
        stage1.set_trade_result(self.entrust, status, price, filled, fees)
        self.stages.append(stage1)

    def add_stage(self, action, status, price, filled, fees):
        idx = len(self.stages) + 1
        if idx == 1:
            print("trade action must be the first stage")
            return False
        if action > 10:
            print("trade action can only be the first one")
            return False

        stage1 = StageInfo(f"stage{idx}")
        stage1.test_action = action
        if action == TestAction.CANCEL:
            stage1.set_cancel_parameters(self.entrust)
            stage1.set_trade_result(self.entrust, status, price, filled, fees)
        else:
            stage1.set_entrust_update(self.entrust, status, price, filled, fees)

        self.stages.append(stage1)

    def toDict(self):
        results = []
        for stage in self.stages:
            results.append(stage.toDict())

        return results

