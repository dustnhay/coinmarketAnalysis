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
