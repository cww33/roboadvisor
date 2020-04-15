import os
#import pytest

from roboadvisor import to_usd, get_response

CI_ENV = os.environ.get("CI")==True

def test_get_response(): #Professor's Test code
    symbol="goog"

    parsed_response = get_response(symbol)
    assert isinstance(parsed_response, dict)
    assert "Meta Data" in parsed_response.keys()
    assert "Time Series (Daily)" in parsed_response.keys()
    assert parsed_response["Meta Data"]["2. Symbol"]==symbol

def test_to_usd(): #My Shopping_cart test code
    result= to_usd(73498.82)
    assert result == "$73,498.82"
    assert to_usd(9.8) == "$9.80"


    #below test does not work because my formatting of the data does not come until after I try to write the data into the csv file. 
    #In my roboadvisor.py I don't format the data until I am writing the rows of the csv file and I finished this test hoping it will run but it runs into errors.

#def test_data_format_csv():
#    parsed_response= {"Meta Data": {
#        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
#        "2. Symbol": "goog",
#        "3. Last Refreshed": "2020-04-14",
#        "4. Output Size": "Compact",
#        "5. Time Zone": "US/Eastern"
#    },
#    "Time Series (Daily)": {
#        "2020-04-14": {
#            "1. open": "1245.0900",
#            "2. high": "1282.0700",
#            "3. low": "1236.9300",
#            "4. close": "1269.2300",
#            "5. volume": "2446681"
#        },
#        "2020-04-13": {
#            "1. open": "1209.1800",
#            "2. high": "1220.5100",
#            "3. low": "1187.6000",
#            "4. close": "1217.5600",
#            "5. volume": "1739828"
#        },
#        "2020-04-09": {
#            "1. open": "1224.0800",
#            "2. high": "1225.5700",
#            "3. low": "1196.7400",
#            "4. close": "1211.4500",
#            "5. volume": "2175421"
#        },
#        "2020-04-08": {
#            "1. open": "1206.5000",
#            "2. high": "1219.0700",
#            "3. low": "1188.1600",
#            "4. close": "1210.2800",
#            "5. volume": "1975135"
#        },
#        "2020-04-07": {
#            "1. open": "1221.0000",
#            "2. high": "1225.0000",
#            "3. low": "1182.2300",
#            "4. close": "1186.5100",
#            "5. volume": "2387329"
#        },
#        "2020-04-06": {
#            "1. open": "1138.0000",
#            "2. high": "1194.6600",
#            "3. low": "1130.9400",
#            "4. close": "1186.9200",
#            "5. volume": "2664723"
#        }}}
#    format_response = [
#        {"timestamp": "2020-04-14", "open": 1245.0900, "high": 1282.0700, "low": 1236.9300, "close": 1269.2300, "volume": 2446681},
#        {"timestamp": "2020-04-13", "open": 1209.1800, "high": 1220.5100, "low": 1187.6000, "close": 1217.5600, "volume": 1739828},
#        {"timestamp": "2020-04-09", "open": 1224.0800, "high": 1225.5700, "low": 1196.7400, "close": 1211.4500, "volume": 2175421},
#        {"timestamp": "2020-04-08", "open": 1206.5000, "high": 1219.0700, "low": 1188.1600, "close": 1210.2800, "volume": 1975135},
#        {"timestamp": "2020-04-07", "open": 1221.0000, "high": 1225.0000, "low": 1182.2300, "close": 1186.5100, "volume": 2387329}
#
#    ]
#
#
#    assert print_to_csv(parsed_response) == format_response
#