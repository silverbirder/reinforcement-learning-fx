#! /usr/bin/python
# -*- coding: utf-8 -*-
u'''
Slackにメッセージ通知するモジュール。

このモジュールを使用する為には、
通知されるslackでslackAppのincomingWebHooksを設定する必要あり。
また、そのアプリはチャネルごとに作成する必要がある。
'''

import json
import requests
from constant import SLACK_POST_URL, SLACK_CHANNEL

class Slack(object):

    def post(self, msg, color='#00ff00'):
        try:
            # default color is green.
            attachments = {
                'text' : msg,
                'color': color,
            }
            slack_contexts = {
                'channel'    : SLACK_CHANNEL,
                'attachments': [attachments],
            }
            req = requests.post(
                SLACK_POST_URL, data=json.dumps(slack_contexts))
            return req
        except Exception as e:
            print(e)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-m',
                      '--msg',
                      type=str,
                      dest='msg',
                      help='post message',
                      default='待たせたな！！')
    (options, args) = parser.parse_args()
    slack = Slack()
    result = slack.post(options.msg)
    print(result)
