import sys,os
sys.path.append(os.pardir)
from etc.db import Db

class Source():
	def __init__(self, db='money', collection='usd_jpy_m5'):
		self.db = Db()
		self.db.set_db('money')
		self.db.set_collection('usd_jpy_m5')

	def read(self):
		return self.db.collection.find()
