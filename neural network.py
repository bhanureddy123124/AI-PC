import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x))


X = np.array([[1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1]])
y = np.array([[1], [0], [0], [0]])


weights1 = np.random.rand(3, 4)
bias1 = np.random.rand(4, 1)
weights2 = np.random.rand(4, 1)
bias2 = np.random.rand(1, 1)


layer1 = sigmoid(np.dot(X, weights1) + bias1)
output = sigmoid(np.dot(layer1, weights2) + bias2)

print(output)
