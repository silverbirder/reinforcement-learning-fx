ACTION = {
	'BUY'  : 1,
	'SELL' : 2,
	'CLOSE': 3,
	'STAY' : 4,
}

OANDA_ACCESS_TOKEN = '01029ebadd7c1bcdb202b0834dfb7ca0-fa84d82e0feb6ec9320d2712182f5b45'

DB = {
	'USER'   : 'admin',
	'PASS'   : 'Okonomiyaki8#',
	'SERVER' : 'cluster0-shard-00-00-z22xi.mongodb.net:27017,cluster0-shard-00-01-z22xi.mongodb.net:27017,cluster0-shard-00-02-z22xi.mongodb.net:27017',
	'PARAM'  : 'test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin',
}

# slackAppのincomingWebHookからURLを取得してください。
SLACK_POST_URL = ''
SLACK_CHANNEL = 'sandbox'
