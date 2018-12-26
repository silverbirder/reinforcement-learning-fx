# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

class DateUtil:
    def make_trade_expire(*, days):
        """ 注文期限を作成する

        Args:
            days: 現在日時からの有効期限までの日数

        Returns:
            有効期限の日時文字列(ex. 2018-01-13T06:57:50.983628Z)
        """
        trade_expire = datetime.utcnow() + timedelta(days = days)
        trade_expire = trade_expire.isoformat("T") + "Z"
        return trade_expire
