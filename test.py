import numpy as np
import pandas as pd
import yfinance as yf

start_date = "2021-05-23"
end_date = "2023-05-23"


data = yf.download("^NSEI", start=start_date, end=end_date)

tenkan_sen = (np.max(data['High'].rolling(window=9).max()) + np.min(data['Low'].rolling(window=9).min())) / 2

kijun_sen = (np.max(data['High'].rolling(window=26).max()) + np.min(data['Low'].rolling(window=26).min())) / 2

senkou_span_a = ((tenkan_sen + kijun_sen) / 2)

senkou_span_b = ((np.max(data['High'].rolling(window=52).max()) + np.min(data['Low'].rolling(window=52).min())) / 2)

cloud_data = pd.DataFrame(index=data.index)
cloud_data['Tenkan-sen'] = tenkan_sen
cloud_data['Kijun-sen'] = kijun_sen
cloud_data['Senkou Span A'] = senkou_span_a
cloud_data['Senkou Span B'] = senkou_span_b
print(cloud_data)

