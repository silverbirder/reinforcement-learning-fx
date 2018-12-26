# -*- coding: utf-8 -*-
import sys
from os import path
from pprint import pprint

class _const(object):
    """
    疑似的に定数を表現する為のクラス
    ※ クラス名は`_ファイル名`にしておく事
    """
    class ConstError(TypeError):pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)" % name)
        self.__dict__[name] = value
        def __delattr__(self, name):
            if name in self.__dict__:
                raise self.ConstError("Can't unbind const(%s)" % name)
            raise NameError(name)

sys.modules[__name__] = _const()


# 定数
from config import const as Const

""" ディレクトリ関係 """
# アプリケーション ルート
Const.APP_ROOT = path.dirname( path.abspath( __file__ ) ) + '/../'
# Config ディレクトリ
Const.CONFIG_DIR = Const.APP_ROOT + 'config/'

""" ファイル関係 """
# アカウント設定ファイル
Const.ACCOUNT_YML = Const.CONFIG_DIR + 'account.yml'

""" 通貨ペア """
class Pair(): pass
pair = Pair()
pair.USD_JPY = 'USD_JPY'
pair.AUD_CAD = 'AUD_CAD'
Const.PAIR = pair

""" 取引種別 """
class DealType(): pass
deal_type = DealType()
deal_type.BUY = 'buy' # 買建
deal_type.SELL = 'sell' # 売建
Const.DEAL_TYPE = deal_type

""" 注文種別 """
class OrderType(): pass
order_type = OrderType()
order_type.LIMIT = 'limit' # 指値
order_type.MARKET = 'market' # 成行
Const.ORDER_TYPE = order_type
