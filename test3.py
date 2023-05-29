import pandas as pd
import yfinance as yf

# Define the ticker symbol for Nifty 50
ticker = "^NSEI"

# Define the start and end dates for the analysis
start_date = "2021-05-23"
end_date = "2023-05-23"

# Get historical data from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate the typical price
data['Typical Price'] = (data['High'] + data['Low'] + data['Close']) / 3

# Set the window size and multiplier for the Keltner Channels
window_size = 20
multiplier = 1.5

# Calculate the EMA of the typical price
data['EMA'] = data['Typical Price'].ewm(span=window_size).mean()

# Calculate the average true range (ATR)
data['ATR'] = data['High'] - data['Low']
data['ATR'] = data['ATR'].ewm(span=window_size).mean()

# Calculate the upper and lower bands of the Keltner Channels
data['Upper Band'] = data['EMA'] + (multiplier * data['ATR'])
data['Lower Band'] = data['EMA'] - (multiplier * data['ATR'])

# Select the desired columns for analysis
keltner_channels = data[['Typical Price', 'Upper Band', 'Lower Band']]

# Print the Keltner Channels
print(keltner_channels)
