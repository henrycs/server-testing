"""Main module."""
import datetime
import logging
import uuid
from typing import Dict, List
from servertester.sdk.transport import get, post_json
from servertester.sdk.trade import OrderSide, OrderType


logger = logging.getLogger(__name__)

class TradeClient:
    def __init__(self, url: str, acct: str, token: str):
        """构建一个交易客户端

        当`is_backtest`为True时，会自动在服务端创建新账户。此时kwargs必须传入capital和commission。

        Info:
            如果`url`指向了回测服务器，但`is_backtest`设置为False，如果提供的账户acct,token在服务器端存在，则将重用该账户，该账户之前的一些数据仍将保留，这可能导致某些错误，特别是继续进行测试时，时间发生rewind的情况。

        Args:
            url : 服务器地址及路径，比如 http://localhost:port/trade/api/v1
            acct : 子账号
            token : 子账号对应的服务器访问令牌
            is_backtest : 是否为回测模式，默认为False。

        Raises:
            CreateAccountError 如果创建账户失败，则会抛出些异常。
        """
        self._url = url.rstrip("/")
        self.token = token
        self.account = acct
        self.headers = {"Authorization": self.token}
        self.headers["Account"] = self.account

    def _cmd_url(self, cmd: str) -> str:
        return f"{self._url}/{cmd}"

    def basic_info(self) -> Dict:
        """获取账户信息

        Returns:
            主要字段：账号名，当前资产，本金，最后一笔交易时间，交易笔数，账户创建时间
        """
        url = self._cmd_url("basic_info")
        try:
            return get(url, headers=self.headers)
        except Exception as e:
            logger.error("info: failed to get information: %s", str(e))
            return None

    def positions(self, dt: datetime.date = None) -> List:
        """取该子账户当前持仓信息

        Args:
            dt : 指定日期，默认为None，表示取当前日期（最新）的持仓信息
        Returns:
            List: 单个股票的信息为，代码，名称，总股数，可卖数，成本均价
        """
        url = self._cmd_url("full_positions")
        if dt is None:
            dt = datetime.date.today()
        datestr = dt.strftime("%Y-%m-%d")
        try:
            return get(url, params={"date": datestr}, headers=self.headers)
        except Exception as e:
            logger.error("positions: failed to get information, %s", str(e))
            return None

    def today_entrusts(self) -> List:
        """查询账户当日所有委托，包括失败的委托

        Returns:
            List: 委托信息数组，字段参考buy
        """
        url = self._cmd_url("today_entrusts")
        try:
            return get(url, headers=self.headers)
        except Exception as e:
            logger.error("today_entrusts: failed to get information, %s", str(e))
            return None

    def stock_pool(self) -> List:
        """查询子账号的股票池

        Returns:
            List: 股票信息
        """
        url = self._cmd_url("stock_pool")
        try:
            return get(url, headers=self.headers)
        except Exception as e:
            logger.error("today_trades: failed to get information, %s", str(e))
            return None

    def cancel_entrust(self, cid: str) -> Dict:
        """撤销委托

        Args:
            cid (str): 交易服务器返回的委托合同号

        Returns:
            Dict: _description_
        """
        url = self._cmd_url("cancel_entrust")

        data = {"cid": cid}
        try:
            return post_json(url, params=data, headers=self.headers)
        except Exception as e:
            logger.error("cancel_entrust: failed to get information, %s", str(e))
            return None

    def buy(
        self, security: str, price: float, volume: int, timeout: float = 0.5, **kwargs
    ) -> Dict:
        """证券买入

        Args:
            security (str): 证券代码
            price (float): 买入价格（限价）
            volume (int): 买入股票数
            timeout (float, optional): 默认等待交易反馈的超时为0.5秒

        Returns:
            Dict: _description_
        """
        if volume != volume // 100 * 100:
            volume = volume // 100 * 100
            logger.warning("买入数量必须是100的倍数, 已取整到%d", volume)

        url = self._cmd_url("buy")
        parameters = {
            "security": security,
            "price": price,
            "volume": volume,
            "timeout": timeout,
            **kwargs,
        }

        try:
            return post_json(url, params=parameters, headers=self.headers)
        except Exception as e:
            logger.error("buy: failed to get information, %s", str(e))
            return None

    def market_buy(
        self,
        security: str,
        volume: int,
        order_type: OrderType = OrderType.MARKET,
        limit_price: float = None,
        timeout: float = 0.5,
        **kwargs,
    ) -> Dict:
        """市价买入股票，同花顺终端需要改为涨跌停限价，掘金客户端支持市价交易，掘金系统默认五档成交剩撤

        Args:
            security (str): 证券代码
            volume (int): 买入数量
            order_type (OrderType, optional): 市价买入类型，缺省为五档成交剩撤.
            limit_price (float, optional): 剩余转限价的模式下，设置的限价
            timeout (float, optional): 默认等待交易反馈的超时为0.5秒

        Returns:
            Dict: _description_
        """

        if volume != volume // 100 * 100:
            volume = volume // 100 * 100
            logger.warning("买入数量必须是100的倍数, 已取整到%d", volume)

        url = self._cmd_url("market_buy")
        parameters = {
            "security": security,
            "price": 0,
            "volume": volume,
            "order_type": order_type,
            "timeout": timeout,
            **kwargs,
        }
        if limit_price is not None:
            parameters["limit_price"] = limit_price

        try:
            return post_json(url, params=parameters, headers=self.headers)
        except Exception as e:
            logger.error("market_buy: failed to get information, %s", str(e))
            return None

    def sell(
        self, security: str, price: float, volume: int, timeout: float = 0.5, **kwargs
    ) -> Dict:
        """以限价方式卖出股票

        Args:
            security (str): 证券代码
            price (float): 买入价格（限价）
            volume (int): 买入股票数
            timeout (float, optional): 默认等待交易反馈的超时为0.5秒
        """
        url = self._cmd_url("sell")
        parameters = {
            "security": security,
            "price": price,
            "volume": volume,
            "timeout": timeout,
            **kwargs,
        }

        try:
            return post_json(url, params=parameters, headers=self.headers)
        except Exception as e:
            logger.error("sell: failed to get information, %s", str(e))
            return None

    def market_sell(
        self,
        security: str,
        volume: int,
        order_type: OrderType = OrderType.MARKET,
        limit_price: float = None,
        timeout: float = 0.5,
        **kwargs,
    ) -> Dict:
        """市价卖出股票，同花顺终端需要改为涨跌停限价，掘金客户端支持市价交易，掘金系统默认五档成交剩撤

        Args:
            security (str): 证券代码
            volume (int): 卖出数量
            order_type (OrderType, optional): 市价卖出类型，缺省为五档成交剩撤.
            limit_price (float, optional): 剩余转限价的模式下，设置的限价
            timeout (float, optional): 默认等待交易反馈的超时为0.5秒
        """
        url = self._cmd_url("market_sell")
        parameters = {
            "security": security,
            "price": 0,
            "volume": volume,
            "order_type": order_type,
            "timeout": timeout,
            **kwargs,
        }
        if limit_price is not None:
            parameters["limit_price"] = limit_price

        try:
            return post_json(url, params=parameters, headers=self.headers)
        except Exception as e:
            logger.error("market_sell: failed to get information, %s", str(e))
            return None
