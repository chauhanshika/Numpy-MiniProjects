import numpy as np

np.random.seed(42)

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [1], [1], [0]])

W1 = np.random.rand(2, 3)
b1 = np.zeros((1, 3))

W2 = np.random.rand(3, 1)
b2 = np.zeros((1, 1))

learning_rate = 0.1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# training loop
for epoch in range(5000):
    # forward
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(a1, W2) + b2
    output = sigmoid(z2)

    # loss
    loss = np.mean((y - output) ** 2)

    # backward
    d_output = (y - output) * sigmoid_derivative(output)

    d_hidden = np.dot(d_output, W2.T) * sigmoid_derivative(a1)

    # update weights
    W2 += learning_rate * np.dot(a1.T, d_output)
    b2 += learning_rate * np.sum(d_output, axis=0, keepdims=True)

    W1 += learning_rate * np.dot(X.T, d_hidden)
    b1 += learning_rate * np.sum(d_hidden, axis=0, keepdims=True)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

print("\nFinal Predictions:\n", output)
