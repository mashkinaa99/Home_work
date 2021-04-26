stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

result = 0

for stock_key, stock_value in stock.items():
    for prices_key, prices_value in prices.items():
        if prices_key == stock_key:
            result += stock_value * prices_value

print(result)