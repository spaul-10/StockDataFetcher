from nsetools import Nse

nse = Nse()
stock_codes = nse.get_stock_codes()

# Display stock symbols
print(stock_codes)
with open("stock_codes.txt", "w") as file:
    for stock in stock_codes:
        file.write(stock + "\n")

        