import numpy as np

temperatures = np.array([
30, 32, 31, 29, 28, 35, 36, 37, 34, 33,
31, 30, 29, 28, 27, 26, 32, 34, 36, 38,
37, 35, 33, 32, 31, 29, 28, 27, 26, 30
])

avg_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

# Heatwave detection
heatwave_days = temperatures[temperatures > 35]

# Cold day detection
cold_days = temperatures[temperatures < 15]

print("\nWeather Data Analysis\n")

print("Average Temperature:", avg_temp, "°C")
print("Hottest Day:", max_temp, "°C")
print("Coldest Day:", min_temp, "°C")

print("\nHeatwave Days (>35°C):", len(heatwave_days))
print("Cold Days (<15°C):", len(cold_days))
