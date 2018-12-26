# -*- coding: utf-8 -*-
from abc import *

# Broker 抽象クラス
class AbstractBroker(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        """ 注文の実行 """
        raise NotImplementedError()

    @abstractmethod
    def sell(self):
        """ 新規売り注文 """
        raise NotImplementedError()

    @abstractmethod
    def buy(self):
        """ 新規買い注文 """
        raise NotImplementedError()

    @abstractmethod
    def modify_order(self):
        """ 注文変更 """
        raise NotImplementedError()

    @abstractmethod
    def cancel_order(self):
        """ 注文キャンセル """
        raise NotImplementedError()

    @abstractmethod
    def load_orders(self):
        """ 注文取得 """
        raise NotImplementedError()

    @abstractmethod
    def modify_position(self):
        """ 玉建変更 """
        raise NotImplementedError()

    @abstractmethod
    def close_position(self):
        """ 玉建決済 """
        raise NotImplementedError()

    @abstractmethod
    def load_positions(self):
        """ 玉建取得 """
        raise NotImplementedError()
