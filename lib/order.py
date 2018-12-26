# -*- coding: utf-8 -*-
class Order():

    def __init__(self, **params):
        # 通貨ペア
        self.instrument = params.get('instrument')
        # 取引単位数
        self.units = params.get('units')
        # 取引種別(買建 or 売建)
        self.side = params.get('side')
        # 注文種別(指値, 成行 etc...)
        self.type = params.get('type')
        # 価格
        self.price = params.get('price')
        # 有効期限
        self.expiry = params.get('expiry')

    def send(self, action):
        # ToDo
        pass
