#pip install pymongo
#pip install schedule
#db.allTimeData.find({},{"athigh_usd":1})
#mongoimport --host ds127126.mlab.com:27126 --db mountain --collection coinMarketCap -u germ -p blueelephant --type json --jsonArray --file /Users/devendra_behera/mygit/coinmarketAnalysis/coin_data_sample.json
import requests
import time
from datetime import datetime
import json
from pymongo import MongoClient
while True:
	startTime = datetime.now()
	client = MongoClient("mongodb://germ:blueelephant@ds127126.mlab.com:27126/mountain")
	db = client.mountain
	all_coins_data = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=600").json()
	for item in all_coins_data:
		db.coinMarketCap.insert(item)
	print db.coinMarketCap.find().count()
	print datetime.now() - startTime
	time.sleep(300)

#db.coinMarketCap.bulk. te()
