# import yfinance as yf  

# # Fetch stock data  
# with open("stock_codes.txt", "r") as file:  
#     for line in file:  
#         a = line.strip()  # Remove any extra spaces or newline characters  

# print(f"{a}.NS")  
# stock = yf.Ticker(f"{a}.NS")  # ".NS" indicates it's listed on NSE  
# data = stock.history(period="max")  # Fetch full historical data  

# # Fetch corporate actions (dividends & stock splits)
# actions = stock.actions  

# # Save historical data and corporate actions to CSV
# data.to_csv(f"{a}_stock_data.csv")  
# actions.to_csv(f"{a}_corporate_actions.csv")  

import os  
import yfinance as yf  

# Specify the folder where you want to save the files  
update_folder = "C:/Users/USER/Desktop/IT/STOCK DAILY DATA"  # Update this path as needed  
save_folder = "C:/Users/USER/Desktop/IT/STOCK CORPORATE ACTIONS"  # Update this path as needed 
# Ensure the folder exists  
os.makedirs(save_folder, exist_ok=True)  

# Fetch stock data  
with open("stock_codes.txt", "r") as file:  
    for line in file:  
        a = line.strip()  # Remove any extra spaces or newline characters  

        print(f"{a}.NS")  
        stock = yf.Ticker(f"{a}.NS")  # ".NS" indicates it's listed on NSE  
        # data = stock.history(period="max")  # Fetch full historical data  

        # Fetch corporate actions (dividends & stock splits)  
        actions = stock.actions  

        # Save files in the specified folder  
        # data.to_csv(os.path.join(update_folder, f"{a}_stock_data.csv"))  
        actions.to_csv(os.path.join(save_folder, f"{a}_corporate_actions.csv"))  