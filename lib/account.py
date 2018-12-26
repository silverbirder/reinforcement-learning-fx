# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.pardir)
from etc import constant
from config import const as Const
import yaml

class Account():

    def __init__(self):
        # アカウントID
        self.account_id = None
        # アクセストークン
        self.access_token = ''

        with open(Const.ACCOUNT_YML) as file:
            obj = yaml.load(file)
            oanda = obj['oanda']

            self.account_id = oanda['account_id']
            self.access_token = oanda['access_token']
