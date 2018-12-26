import sys,os
sys.path.append(os.pardir)
from etc import constant
import pymongo

class Db():
	def __init__(self):
		url = 'mongodb://%s:%s@%s/%s' % (constant.DB['USER'], constant.DB['PASS'], constant.DB['SERVER'], constant.DB['PARAM'])
		self.client = pymongo.MongoClient(url)
		self.db = None
		self.collection = None

	def set_db(self, name):
		self.db = self.client[name]

	def set_collection(self, name):
		self.collection = self.db[name]