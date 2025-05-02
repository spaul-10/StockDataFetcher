import yfinance as yf

# Fetch SBIN stock data

sbin = yf.Ticker("motherson.NS")  # ".NS" indicates it's listed on NSE
data = sbin.history(period="max")  # Last 1 month of data

# Display Open, High, Low, Close prices
print(data[['Open', 'High', 'Low', 'Close']])
data.to_csv("AAPL_stock_data.csv")


