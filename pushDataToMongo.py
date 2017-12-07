#pip install pymongo
#pip install schedule
#db.allTimeData.find({},{"athigh_usd":1})
#mongoimport --host ds127126.mlab.com:27126 --db mountain --collection coinMarketCap -u germ -p blueelephant --type json --jsonArray --file /Users/devendra_behera/mygit/coinmarketAnalysis/coin_data_sample.json
import requests
import time
from datetime import datetime
import json
from pymongo import MongoClient
#db.coinMarketCap.bulk. te()
def pushData():
#should push the data to mongo every 5 mins. This is better achieved by the import.Can set up a cron job 
#rather than iterating over the list array and writing to the db multiple times
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
#def sendMail(coin_list):
#should send a mail to the registered mail ids with the list details
def findATH():
#shold giv a list of coins which are nearing ath and also update the collection with the
#the new ath/atl value if it has breached
#should return a list of coin ids which are nearing ath.atl
	client = MongoClient("mongodb://germ:blueelephant@ds127126.mlab.com:27126/mountain")
	db = client.mountain
	currentPrices={} #stores the current usd price from get response from the coinmarketcap api
	all_time_highlow_prices = {} # gets the data from the mongo collection
	all_coins_data = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=600").json()
	for item in all_coins_data:
		currentPrices[item["id"]]=item["price_usd"]
	print currentPrices
	all_time_doc_data=db.allTimeData.find({},{"athigh_usd":1})
	for doc in all_time_doc_data:
		all_time_highlow_prices[doc['_id']] = doc['athigh_usd']
	print all_time_highlow_prices


if __name__ == '__main__':
	findATH()