#http://tiborsimko.org/postgresql-mongodb-json-select-speed.html
#"athigh_usd":"15971.00",
#"id": "bitcoin", 
import requests
import json
from pymongo import MongoClient
client = MongoClient("mongodb://germ:blueelephant@ds127126.mlab.com:27126/mountain")
db = client.mountain
currentPrices = {}
all_coins_data = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=0").json()
for item in all_coins_data:
 print "\t{"
 print '\t"id" : "'+item["id"]+'",'
 print '\t"name" : "'+item["name"]+'",'
 print '\t"rank" : "'+item["rank"]+'",'
 print '\t"ATHigh_usd" : "'+item["price_usd"]+'",'
 print '\t"ATHigh_btc" : "0.00000000",'
 print '\t"ATHigh_btc_epoc" : "",'
 print '\t"ATLow_usd" : "0.00",'
 print '\t"ATLow_btc" : "0.00000000",'
 print '\t"ATLow_btc_epoc" : "",'
 print '\t},'
		#+, item["id"],item["id"]
		#currentPrices[item["id"]]=item["price_usd"]
#print currentPrices

		#db.coinMarketCap.insert(item)
#curl_output = curl("https://api.coinmarketcap.com/v1/ticker/?limit=0")
#print type(curl_output)
#all_coins_data =  requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=0").json()
#print type (all_coins_data)
#print all_coins_data[0]
#json_obj_array= all_coins_data.json
#x=db.allTimeData.find({},{"athigh_usd":1})
#for doc in x:
#	print doc['_id'], doc['athigh_usd']
"""x = '''
    {
        "id": "bitcoin", 
        "name": "Bitcoin", 
        "symbol": "BTC", 
        "rank": "1", 
        "price_usd": "11739.8", 
        "price_btc": "1.0", 
        "24h_volume_usd": "5308920000.0", 
        "market_cap_usd": "196255257963", 
        "available_supply": "16717087.0", 
        "total_supply": "16717087.0", 
        "max_supply": "21000000.0", 
        "percent_change_1h": "0.52", 
        "percent_change_24h": "5.28", 
        "percent_change_7d": "28.95", 
        "last_updated": "1512306253"
    }, 
    {
        "id": "ethereum", 
        "name": "Ethereum", 
        "symbol": "ETH", 
        "rank": "2", 
        "price_usd": "480.79", 
        "price_btc": "0.0411767", 
        "24h_volume_usd": "810612000.0", 
        "market_cap_usd": "46207489076.0", 
        "available_supply": "96107425.0", 
        "total_supply": "96107425.0", 
        "max_supply": null, 
        "percent_change_1h": "-0.21", 
        "percent_change_24h": "3.05", 
        "percent_change_7d": "4.36", 
        "last_updated": "1512306252"
    }
    '''
print x


db = client.mountain
db.coinMarketCap.insert([])
x = db.coinMarketCap.find()
print x.count()
"""
