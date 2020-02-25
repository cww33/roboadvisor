# Robo Advisor Project

## Setup

### Repo Setup

Use Github.com online interface a new remote repository such as *robo_advisor*. Ensure you add a "README.md" file and a ".gitignore" file. Using the dropdown menu pick the option that says Python.

After creating the remote repo, use the Github.com online interface and click on the green button that says Clone or Download and click on the option that says Open in Desktop. Once this is done you will be promted on your web browser asking if you want to open the repository on your Github desktop software, click on the option that says Open GitHubDesktop.exe.

After you finish that, navigate to the repo from the command line:

```
cd ~/Desktop/robo_advisor
```

Create a new file in your project called *requirements.txt* and then place the following contents inside:

```
requests
python-dotnev
```
These packages will be installed after the virtual environment is set up.

###Environment Setup

We need to create and activate a new Anaconda virtual environment. Do this by first placing in the command line:

```
conda create -n stocks-env python=3.7
```
This will only be done when setting up the project for the first time. Run it and then place in the command line:

```
conda activate stocks-env
```
This will activate the virtual environment. From within the virtual environment, demonstrate your ability to run the Python script from the command line:
```
python app/robo_advisor.py
```

### Program Output

This program will produce a output similar to:

```
-------------------------
SELECTED SYMBOL: GOOG # YOUR CHOSEN SYMBOL
-------------------------
REQUESTING STOCK MARKET DATA...
REQUEST AT: 02/24/2020 06:57 PM # THE TIME YOU REQUESTED THE DATA
-------------------------
LATEST DAY: 2020-02-24 # THE LATEST DAY THE DATA WAS UPDATED
LATEST CLOSE: $1,421.59 # THE LATEST CLOSING PRICE
RECENT HIGH: $1,532.11 # THE HIGHEST PRICE IN THE LAST 100 DAYS
RECENT LOW: $1,162.43 # THE LOWEST PRICE IN THE LAST 100 DAYS
-------------------------
RECOMMENDATION: Don't Buy. # PROGRAM CALCULATED RECOMMENDATION
RECOMMENDATION REASON: Since the stock's most recent closing price was was greater than 20 percent from its recent low, you should not buy! # RECOMMENDATION REASONING
-------------------------
Writing data to CSV file: app\..\data\prices.csv...
-------------------------
HAPPY INVESTING!
-------------------------
```


### Potential Errors and What they Mean

#### "Sorry expecting a properly-formed stock symbol like 'MSFT'. Please try again."

This means that your inputed stock symbol is incorret please check it and run the program again. Ensure all your characters inputted are correct and your stock symbol is between (not including) 2 and 6 characters long. In addition, the program will not read any numbers and will also return this same message.

#### "Sorry, couldn't find any trading data for that stock symbol"

This means that even though your stock symbol is inputted in a format that the program can read, the program can either not be able to find the proper data, or the stock symbol has an error on it and this stock does not exist. If this happens to you, re-run the program and ensure your stock symbol is correct.

### Informational Output

All information that on the stock symbol you chose will be inputted into a csv file named: *prices.csv* under the data folder. It will include data on the *timestamp, open price, high price, low price, close price* and *volume*.

### Recomendation 

#### Disclaimer

A recomendation of either *"Buy!"* or *"Don't Buy."* will be given by the program. This is merely a recommendation, even though the program will perform its function without fail, it is a program that recommends, and it is not able to predict the future. Buy stocks at your own risk. 

#### How the Recommendation is Calculated (in pseudocode)

If the stock's latest closing price is less than 20% above its recent low, "Buy!", else "Don't Buy.". 




