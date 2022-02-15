#imports
import pandas as pd
import re
import json
import requests
from pathlib import Path
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

#reading csv data into a dataframe
print("Enter File Path")
file_getter = Path(input())
data = pd.read_csv(file_getter)

#obtaining API data from CoinGecko
API_id_list = data['API id'].tolist()
API_response = cg.get_coins_markets(vs_currency='usd', ids=API_id_list)


#create empty lists for data
current_price = []
circulating_supply = []
total_supply = []
missing = []

#loop through dataframe and API_response list to append data
for entry in data['API id']:
    found = 'N'
    for item in API_response:
        if item['id'] == entry:
            found = 'Y'
            current_price.append(item['current_price'])
            circulating_supply.append(item['circulating_supply'])
            total_supply.append(item['total_supply'])
    #if item not found on coingecko, appending token to missing list and N/A to data
    if found == 'N':
        current_price.append(None)
        circulating_supply.append(None)
        total_supply.append(None)
        missing.append(entry)

#appending price data to the data dataframe
data['current price'] = current_price

#obtaining total crypto holdings and holdings for each owner by multiplying by current price column
data['owner1 token value'] = data['owner1'] * data['current price']
data['owner2 token value'] = data['owner2'] * data['current price']
data['owner3 token value'] = data['owner3'] * data['current price']
data['owner4 token value'] = data['owner4'] * data['current price']
data['total'] = data['owner1 token value'] + data['owner2 token value'] + data['owner3 token value'] + data['owner4 token value']

print(data)
#generate plots



