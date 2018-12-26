# -*- coding: utf-8 -*-
"""
ツール群
(現状は動作確認に利用しています。)
"""

import sys
import argparse
import oandapy
import time
from pprint import pprint
from datetime import datetime, timedelta

from lib.account import Account
from config import const as Const
from lib.order import Order
from lib.broker.real_broker import RealBroker
from util.date_util import DateUtil

account = Account()
oanda = oandapy.API(environment = "practice", access_token = account.access_token)

def fetch_accounts_list():
    """ アカウント一覧取得 """
    response = oanda.get_accounts()
    print(response)

def fetch_account():
    """ アカウント取得 """
    response = oanda.get_account(account.account_id)
    print(response)

def fetch_orders_list():
    """ オーダー一覧 """
    response = oanda.get_orders(account.account_id)
    print(response)

def fetch_streaming_rate():
    """ ストリーミングレート取得 """
    print("#fetch_streaming_rate")

    while(True):
        time.sleep(1)
        response = oanda.get_prices(instruments = Const.PAIR.USD_JPY)
        prices = response.get("prices")
        print(prices[0])

def execute_create_order():
    """
    オーダー
    ※ 成行は営業時間中しか出せない(error code 24)
    """
    trade_expire = datetime.utcnow() + timedelta(days = 5)
    trade_expire = trade_expire.isoformat("T") + "Z"
    print(trade_expire)
    response = oanda.create_order(account.account_id,
                                  instrument = Const.PAIR.USD_JPY,
                                  units = 1000,
                                  side = Const.DEAL_TYPE.BUY,
                                  type = Const.ORDER_TYPE.LIMIT,
                                  price = 110.0,
                                  expiry = trade_expire)
    print(response)

def check_real_broker():
    """ Brokerモデルの動作確認 """
    # 注文作成
    order = Order(instrument = Const.PAIR.USD_JPY,
                  units = 1000,
                  side = Const.DEAL_TYPE.BUY,
                  type = Const.ORDER_TYPE.LIMIT,
                  price = 98.3,
                  expiry = DateUtil.make_trade_expire(days = 6))

    # 注文実行
    broker = RealBroker()
    broker.execute(order)

if __name__ == '__main__':
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description = "Auto Order Tools")
    parser.add_argument("-k", type=str, help = "実行する関数のキー", required=True)

    command_arguments = parser.parse_args()
    tool_key = command_arguments.k

    tools = {
        'fal': fetch_accounts_list,
        'fa': fetch_account,
        'fol': fetch_orders_list,
        'fsr': fetch_streaming_rate,
        'eco': execute_create_order,
        'crb': check_real_broker,
    }

    if not tool_key in tools.keys():
        print("引数に間違いがあります")
        quit()

    # 指定された関数の実行
    tools[tool_key]()
