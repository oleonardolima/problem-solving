n_days = input()
stock_prices = input()
stock_prices = list(stock_prices.split(" "))
stock_prices = [int(price) for price in stock_prices]

print(stock_prices)

ptr1 = 0
ptr2 = 2

n_stocks = 0
total_amount = 0
while ptr2 < n_days:
    print("ptr1: {}".format(ptr1))
    print("ptr2: {}".format(ptr2))
    if ptr1 == ptr2:
        ptr2 += 1
    elif stock_prices[ptr1] > stock_prices[ptr2] and n_stocks == 0:
        ptr1 += 1
        ptr2 += 1
    
    elif stock_prices[ptr1] < stock_prices[ptr2]:
        print(stock_prices[ptr1])
        print(stock_prices[ptr2])
        n_stocks += 1
        total_amount -= stock_prices[ptr1]
        ptr1 += 1
    else:
        ptr1 += 1

print(total_amount)
