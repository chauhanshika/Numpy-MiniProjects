import numpy as np

# user-item interaction matrix
# rows = users
# columns = items
ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
    [0, 1, 5, 4]
])

print("User-Item Matrix:\n")
print(ratings)
