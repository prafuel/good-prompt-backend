from pymongo import MongoClient
import os

import numpy as np

from dotenv import load_dotenv
load_dotenv()

url = os.environ['MONGO_URL']
db = os.environ['DB']

class Mongo:
	def __init__(self) -> None:
		client = MongoClient(url)
		self.db = client[db]

	def get(self, collection:str):
		data = self.db[collection]

		items = []
		for item in data.find():
			item.pop("_id")
			items.append(item)
		return items

	def put(self, collection:str):
		pass

if __name__ == "__main__":
	table = "prebuiltPrompts"
	obj = Mongo()
	print(obj.get(table))
