import numpy as np
import pandas as pd
import yfinance as yf


start_date = '2021-05-23'
end_date = '2023-05-23'


data = yf.download('^NSEI', start=start_date, end=end_date)


typical_price = (data['High'] + data['Low'] + data['Close']) / 3


distance_moved = typical_price.diff(1)


box_ratio = data['Volume'] / (data['High'] - data['Low'])


eom = distance_moved / box_ratio


print(eom)