def buy_sell(price):
    min_profit = price[0]
    max_profit = 0
    for i in price:
        if i < min_profit:
            min_profit = i
        if i - min_profit > max_profit:
            max_profit = i - min_profit
    return max_profit

price = [7,1,5,6,3]
print(buy_sell(price))

