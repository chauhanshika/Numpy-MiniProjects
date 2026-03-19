# Mini Neural Network from Scratch (NumPy)

This project implements a **2-layer neural network from scratch using NumPy**, including forward propagation, backpropagation, and training on a non-linear dataset (XOR problem).

---

## Objective

To understand how neural networks work internally by building one using only NumPy, without relying on machine learning libraries.

---

## Features

* Multi-layer neural network (input → hidden → output)
* Forward propagation
* Sigmoid activation function
* Backpropagation (gradient-based learning)
* Loss calculation (Mean Squared Error)
* Training loop with weight updates
* Learning non-linear patterns (XOR problem)

---

## Dataset

The model is trained on a simple XOR dataset:

```python
X = [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]

y = [[0],
     [1],
     [1],
     [0]]
```

This dataset is commonly used to demonstrate non-linear learning capability in neural networks.

---

## Model Architecture

```text
Input Layer (2 neurons)
        ↓
Hidden Layer (3 neurons, sigmoid)
        ↓
Output Layer (1 neuron, sigmoid)
```

---

## Training Process

* Initialize weights and biases randomly
* Perform forward propagation
* Compute loss using Mean Squared Error
* Apply backpropagation to calculate gradients
* Update weights using gradient descent
* Repeat for multiple epochs

---

## Sample Output

```text
Epoch 0, Loss: 0.25
Epoch 1000, Loss: 0.02
Epoch 2000, Loss: 0.01

Final Predictions:
[[0.02]
 [0.97]
 [0.97]
 [0.03]]
```

---

## Tech Stack

* Python
* NumPy

---

## Key Concepts Covered

* Matrix multiplication (`np.dot`)
* Activation functions (sigmoid)
* Gradient calculation
* Backpropagation
* Loss minimization
* Neural network training dynamics

---

## Learning Outcome

This project demonstrates how neural networks:

* Learn from data using gradient-based optimization
* Capture non-linear relationships
* Update internal parameters iteratively to reduce error

It provides a strong foundation for understanding advanced deep learning frameworks like TensorFlow and PyTorch.

---

## Repository Structure

```text
Project-9-Mini-Neural-Network
│
├── main.py
├── README.md
├── requirements.txt
└── result9.png
```

---

## Sample Output Screenshot

![Program Output](result9.png)
