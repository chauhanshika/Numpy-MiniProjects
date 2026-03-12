import numpy as np

prices = np.array([100, 102, 101, 105, 107, 106, 108, 110, 109, 111])

avg_price = np.mean(prices)
max_price = np.max(prices)
min_price = np.min(prices)


returns = np.diff(prices)
volatility = np.std(prices)

print("\nStock Data Analysis\n")

print("Prices:", prices)
print("\nAverage Price:", avg_price)
print("Highest Price:", max_price)
print("Lowest Price:", min_price)

print("\nDaily Returns:", returns)
print("Price Volatility:", volatility)
