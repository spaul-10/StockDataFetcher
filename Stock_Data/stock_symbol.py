# Open and read the file\
c = 0
with open("stock_codes.txt", "r") as file:
    for line in file:
        # if c==100:
        #     break
        # c += 1
        stock_symbol = line.strip()  # Remove any extra spaces or newline characters
        print(stock_symbol)
