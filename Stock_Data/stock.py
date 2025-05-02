
import yfinance as yf 

# Fetch SBIN stock data
# c = 0
with open("stock_codes.txt", "r") as file:
    for line in file:
        # if c==10:
        #     break
        # c += 1
        a = line.strip()  # Remove any extra spaces or newline characters
        
        print (f"{a}.NS")
        stock = yf.Ticker(f"{a}.NS")  # ".NS" indicates it's listed on NSE
        data = stock.history(period="max")  # Last 1 month of data

# Display Open, High, Low, Close prices
        # print(data[['Open', 'High', 'Low', 'Close']])
        data.to_csv(f"{a}_stock_data.csv")


