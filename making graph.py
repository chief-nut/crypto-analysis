import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
from datetime import date, timedelta, datetime
import plotly.graph_objects as go

end_date = datetime.now().strftime('%Y-%m-%d')

def get_data(name):                                     #get coin data    
    BTC = yf.Ticker(name)                               
    Coin_Data = BTC.history(period="max")               #get history of coin                                  #get first 5 rows of dataframe
    return Coin_Data

def plot_data(name):
    coin_data_DF = get_data(name)                       #set old func to variable
    open = coin_data_DF['Open']                 #separating by column and plot                      
    high = coin_data_DF['High']
    low = coin_data_DF['Low']
    close = coin_data_DF['Close']
    date = coin_data_DF.index
    
    fig = go.Figure(data=go.Candlestick(x=date,open=open,high=high,low=low,close=close))            #create graph
    fig.show()



plot_data('BTC-GBP')
