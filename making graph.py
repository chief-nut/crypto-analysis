import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
from datetime import date, timedelta

BTC = yf.Ticker('BTC')
BTC_Data = BTC.history(period="max")
BTC_Data.head()
print(BTC_Data)

