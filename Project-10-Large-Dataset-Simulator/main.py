import numpy as np

data = np.random.randint(1, 100, size=1000000)

mean_val = np.mean(data)
max_val = np.max(data)
min_val = np.min(data)

print("Dataset Size:", len(data))
print("Mean:", mean_val)
print("Max:", max_val)
print("Min:", min_val)
