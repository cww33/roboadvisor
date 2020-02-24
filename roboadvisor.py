# app/robo_advisor.py
import requests
import json
import csv
import os
from dotenv import load_dotenv
import datetime
import time
from datetime import datetime
from time import strftime
now=datetime.now()
loadtime= now.strftime("%m/%d/%Y %I:%M %p") #my shopping cart project

load_dotenv

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)




while True:
    symbol = input('Symbol: ')
    if symbol.isalpha(): #stackoverflow
        break
    print("Sorry expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    exit()

    
    



api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)
#print(type(response))
#print(response.status_code)


    

#print(response.text)
#
#quit()



parsed_response = json.loads(response.text)

if json.loads(response.text) == {"Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."}:
    print("Sorry, couldn't find any trading data for that stock symbol")
    exit()


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())
latest_day=dates[0]

latest_close = tsd[latest_day]["4. close"]
#breakpoint()

high_prices=[]
low_prices=[]

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)


csv_file_path = os.path.join(os.path.dirname(__file__), "data", "prices.csv")


csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
   
    for date in dates:
        daily_prices = tsd[date]  
        writer.writerow({
        "timestamp": date,
        "open": daily_prices["1. open"],
        "high": daily_prices["2. high"],
        "low": daily_prices["3. low"],
        "close": daily_prices["4. close"],
        "volume": daily_prices["5. volume"],

        })


rec_price=(float(latest_close)-float(recent_low))/float(recent_low)
#print(rec_price)
if rec_price <= 0.2:
    recomendation="Buy!"
else:
    recomendation ="Don't Buy."

print("-------------------------")
print("SELECTED SYMBOL: "+symbol.upper())
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: "+loadtime)
print("-------------------------")

print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: "+recomendation)
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"Writing data to CSV file: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


#csv_file_path = "prices.csv" # a relative filepath

