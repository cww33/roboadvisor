# app/robo_advisor.py

import json
import csv
import os
import datetime
import time
from datetime import datetime
from time import strftime
now=datetime.now()
loadtime= now.strftime("%m/%d/%Y %I:%M %p") #my shopping cart project
from dotenv import load_dotenv
import requests
load_dotenv()

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

def to_usd(my_price):
    '''
    Converts the numbers into a USD type format.
    
    Example: to_usd(567.22) = $567.22


    '''

    return "${0:,.2f}".format(my_price)
def printout():

    '''
    Prints out the final culmalitive information of the stock market data. Includes a recomendation and an explanation for the recomendation whether or not to buy.
    '''

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
    print("RECOMMENDATION REASON: "+reason)
    print("-------------------------")
    print(f"Writing data to CSV file: {csv_file_path}...")
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")
def get_response(symbol):
    '''
    Pulls the information from the website for the specific stock inputed. It uses the symbol and the api key to download the data. IF the data is not available, the program will stop itself.
    
    '''
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    if json.loads(response.text) == {"Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."}:
        print("Sorry, couldn't find any trading data for that stock symbol")
        exit()
    return parsed_response
def print_to_csv():
    '''
    formats the information into rows and then exports the information to a csv file.
    '''
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
     
def read_response(parsed_response):
   global tsd
   tsd = parsed_response["Time Series (Daily)"]
   
def prices():
    '''
    Calculates the recent highs and lows for the specific stock inputted. It inputs all the relevant information into a list and looks for the max or the min for the respective lists.
    '''
    global recent_high
    global recent_low
    high_prices=[]
    low_prices=[]
    for date in dates:
        high_price = tsd[date]["2. high"]
        high_prices.append(float(high_price))
        low_price = tsd[date]["3. low"]
        low_prices.append(float(low_price))
    recent_high = max(high_prices)
    recent_low = min(low_prices)
if __name__ == "__main__":
    while True:
        symbol = input('Symbol: ')
        if symbol.isalpha() and len(symbol) > 2 and len(symbol) < 6 : #stackoverflow
            break
        print("Sorry expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
        exit()

   
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")


    parsed_response = get_response(symbol)
    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
    read_response(parsed_response)

    dates = list(tsd.keys())

    latest_day=dates[0]

    latest_close = tsd[latest_day]["4. close"]

    prices()

    rec_price=(float(latest_close)-float(recent_low))/float(recent_low)

    if rec_price <= 0.2:
        recomendation="Buy!"
        reason = "Since the stock's most recent closing price was was not greater than 20 percent from its recent low, you should buy!"
    else:
        recomendation ="Don't Buy."
        reason = "Since the stock's most recent closing price was was greater than 20 percent from its recent low, you should not buy!"

    printout()



