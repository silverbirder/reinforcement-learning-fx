# -*- coding: utf-8 -*-
import oandapy
from lib.broker.abstract_broker import *
from lib.account import Account

class RealBroker(AbstractBroker):
    """ Oanda用のBrokerクラス """

    def __init__(self):
        self.account = Account()
        self.oanda = oandapy.API(environment = "practice",
                                 access_token = self.account.access_token)

    def execute(self, order):
        """ 注文を実行する

        Args:
            order: Orderモデル

        Returns:
            注文の実行結果のディクショナリ
        """
        response = self.oanda.create_order(self.account.account_id,
                                           instrument = order.instrument,
                                           units = order.units,
                                           side = order.side,
                                           type = order.type,
                                           price = order.price,
                                           expiry = order.expiry)
        return response
