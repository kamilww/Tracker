import pandas as pd
import os
import requests
from pathlib import Path
import panel as pn
pn.extension('plotly')
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

print("Enter File Path")
file_getter = Path(input())
data = pd.read_csv(file_getter)
print(data.head())



#crypto_portfolio_analysis = pn.Tabs(
    #("Housing Units Per Year", housing_units_per_year()),
    #("Average Housing Costs in San Francisco Per Year", average_housing_costs_column),
    #("Average Prices By Neighborhood", average_prices_neighborhood_column),
    #("Top 10 Most Expensive Neighborhoods", most_expensive_column), 
    #("Neighborhood Map", neighborhood_map()),
    #name="Crypto Portfolio"
#)   


# Serve the# dashboard
#market_analysis.servable()


