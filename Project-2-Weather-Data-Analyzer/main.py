import numpy as np

# Temperature data for 30 days
temperatures = np.array([
30, 32, 31, 29, 28, 35, 36, 37, 34, 33,
31, 30, 29, 28, 27, 26, 32, 34, 36, 38,
37, 35, 33, 32, 31, 29, 28, 27, 26, 30
])

# Average temperature
avg_temp = np.mean(temperatures)

print("Average Temperature:", avg_temp, "°C")
