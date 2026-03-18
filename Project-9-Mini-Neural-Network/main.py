import numpy as np

# dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [1], [1], [0]])

# initialize weights
np.random.seed(42)
W1 = np.random.rand(2, 3)   # input → hidden
b1 = np.zeros((1, 3))

W2 = np.random.rand(3, 1)   # hidden → output
b2 = np.zeros((1, 1))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# forward pass
z1 = np.dot(X, W1) + b1
a1 = sigmoid(z1)

z2 = np.dot(a1, W2) + b2
output = sigmoid(z2)

print("Initial Output:\n", output)
