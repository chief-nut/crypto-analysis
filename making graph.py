import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
from datetime import date, timedelta, datetime

def get_data(name):                                     #get coin data
    end_date = datetime.now().strftime('%Y-%m-%d')      #get todays date
    BTC = yf.Ticker(name)                               
    Coin_Data = BTC.history(period="max")               #get history of coin
    Coin_Data.head()                                    #get first 5 rows of dataframe
    print(Coin_Data)

get_data('BTC-GBP')                                     #get history of btc
get_data('ETH-GBP')
