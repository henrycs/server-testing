from enum import IntEnum
import uuid
from servertester.sdk.trade import OrderSide, OrderType, OrderStatus

class TestAction(IntEnum):
    BUY = 11  # 股票买入
    SELL = 21  # 股票卖出
    MARKET_BUY = 12  # 股票买入
    MARKET_SELL = 22  # 股票卖出
    CANCEL = 0  # 撤单
    UPDATE = 1  # 更新委托


def get_action(action):
    if action == TestAction.BUY:
        return "buy"
    if action == TestAction.MARKET_BUY:
        return "market_buy"
    if action == TestAction.SELL:
        return "sell"
    if action == TestAction.MARKET_SELL:
        return "market_sell"
    if action == TestAction.CANCEL:
        return "cancel_entrust"
    if action == TestAction.UPDATE:
        return "entrust_update"


class Entrust:
    code: str
    price: float
    volume: int
    order_side: OrderSide
    order_type: OrderType
    eid: str
    entrust_no: str

    def __init__(self, code, price, volume, order_side, order_type):
        self.code = code
        self.price = price
        self.volume = volume
        self.order_side = order_side
        self.order_type = order_type

        self.entrust_no = str(uuid.uuid4())
        self.eid = str(uuid.uuid4())


class StageInfo:
    test_action: TestAction
    comment: str
    stage_name: str
    parameters: dict
    trade_result: dict
    entrust_update: dict

    def __init__(self, name):
        self.comment = "this is a automated test"
        self.stage_name = name
    
    def set_trade_action(self, order_side, order_type):
        if order_side == OrderSide.BUY:
            if order_type == OrderType.LIMIT:
                self.test_action = TestAction.BUY
            else:
                self.test_action = TestAction.MARKET_BUY
        if order_side == OrderSide.SELL:
            if order_type == OrderType.LIMIT:
                self.test_action = TestAction.SELL
            else:
                self.test_action = TestAction.MARKET_SELL
    
    def set_trade_parameters(self, entrust):
        self.parameters = {
            "code": entrust.code,
            "price": entrust.price,
            "volume": entrust.volume
        }

    def set_cancel_parameters(self, entrust):
        self.parameters = {
            "entrust_no": entrust.entrust_no,
        }

    def set_trade_result(self, entrust, order_status, price, filled, fees):
        self.trade_result = {
            "code": entrust.code,
            "price": entrust.price,
            "volume": entrust.volume,
            "order_side": entrust.order_side,
            "bid_type": entrust.order_type,
            "time": "2022-03-23 09:09:05.000000",
            "entrust_no": entrust.entrust_no,
            "eid": entrust.eid,
            "status": order_status,
            "filled": filled,
            "average_price": price,
            "fees": fees,
            "reason": "",
            "recv_at": "2022-03-23 09:09:05.000000"
        }

    def set_entrust_update(self, entrust, order_status, price, filled, fees):
        self.entrust_update = {
            "code": entrust.code,
            "price": entrust.price,
            "volume": entrust.volume,
            "order_side": entrust.order_side,
            "bid_type": entrust.order_type,
            "time": "2022-03-23 09:09:05.000000",
            "entrust_no": entrust.entrust_no,
            "eid": entrust.eid,
            "status": order_status,
            "filled": filled,
            "average_price": price,
            "fees": fees,
            "reason": "",
            "recv_at": "2022-03-23 09:09:05.000000"
        }

    def toDict(self):
        if self.test_action == TestAction.UPDATE:
            return {
                "comment": self.comment,
                "stage": self.stage_name,
                "test_action": get_action(self.test_action),
                "entrust_update": self.entrust_update
            }
        else:
            return {
                "comment": self.comment,
                "stage": self.stage_name,
                "test_action": get_action(self.test_action),
                "parameters": self.parameters,
                "trade_result": self.trade_result,
            }

