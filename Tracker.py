#imports
import pandas as pd
import re
import json
import requests
import datetime as dt
from csv import writer
from pathlib import Path
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

#reading csv data into a dataframe
print("Enter Input File Path")
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

#appending date to dataframe
data.insert(0, 'date', dt.datetime.now())

#appending price data to the data dataframe
data['current price'] = current_price

#obtaining total crypto holdings and holdings for each owner by multiplying by current price column
data['owner1 token value'] = data['owner1'] * data['current price']
data['owner2 token value'] = data['owner2'] * data['current price']
data['owner3 token value'] = data['owner3'] * data['current price']
data['owner4 token value'] = data['owner4'] * data['current price']
data['total'] = data['owner1 token value'] + data['owner2 token value'] + data['owner3 token value'] + data['owner4 token value']

#calculating portfolio value per owner and total percent per owner
total_portfolio = data['total'].sum()
owner1_total = data['owner1 token value'].sum()
owner2_total = data['owner2 token value'].sum()
owner3_total = data['owner3 token value'].sum()
owner4_total = data['owner4 token value'].sum()

percent_owner1 = (owner1_total / total_portfolio) * 100
percent_owner2 = (owner2_total / total_portfolio) * 100
percent_owner3 = (owner3_total / total_portfolio) * 100
percent_owner4 = (owner4_total / total_portfolio) * 100

#peak to trough calculation:


#calculating investments by figures
six_fig = 0
five_fig = 0
four_fig = 0
three_fig = 0
two_fig = 0
one_fig = 0
less_than_one_fig = 0

for entry in data['total']:
    if entry >= 100000:
        six_fig+=1
    elif entry >= 10000:
        five_fig+=1
    elif entry >= 1000:
        four_fig+=1
    elif entry >= 100:
        three_fig+=1
    elif entry >= 10:
        two_fig+=1
    elif entry >= 1:
        one_fig+=1
    else:
        less_than_one_fig+=1

#calculating top ten holdings
data_sorted = data.copy()
data_sorted.sort_values(by = 'total', ascending=False, inplace = True)
print(data_sorted)

#calculating top ten values by ecosystem

#calculating % of supply emitted

#saving data to new csv or appends to existing csv
if '/Users/kamilwojnowski/Fintech/Tracker/Dummy Data/dummyfileouput.csv':
    data_sorted.to_csv(path_or_buf='/Users/kamilwojnowski/Fintech/Tracker/Dummy Data/dummyfileoutput.csv', mode='a', index=False, header=False)
else:
    data_sorted.to_csv(path_or_buf='/Users/kamilwojnowski/Fintech/Tracker/Dummy Data/dummyfileouput.csv', mode='w', index=False, header=True)