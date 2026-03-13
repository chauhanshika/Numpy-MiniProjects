import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([50, 55, 65, 70, 75])

m = 5
b = 45

predictions = m * x + b

mse = np.mean((y - predictions) ** 2)

print("\nLinear Regression Analysis\n")

print("Actual Scores:", y)
print("Predicted Scores:", predictions)
print("\nMean Squared Error:", mse)
