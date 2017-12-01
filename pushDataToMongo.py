#pip install pymongo
from pymongo import MongoClient
client = MongoClient("mongodb://germ:blueelephant@ds127126.mlab.com:27126")
db = client.mountain
x=db.coinMarketCap.find()
for doc in x:
	print (doc)
