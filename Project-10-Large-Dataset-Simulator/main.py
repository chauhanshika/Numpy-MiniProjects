import numpy as np
import time

data = np.random.randint(1, 100, size=1000000)

# NumPy computation
start = time.time()
mean_np = np.mean(data)
end = time.time()

print("NumPy Mean:", mean_np)
print("NumPy Time:", end - start)

# Loop computation
start = time.time()
total = 0
for val in data:
    total += val
mean_loop = total / len(data)
end = time.time()

print("\nLoop Mean:", mean_loop)
print("Loop Time:", end - start)
