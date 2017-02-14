import numpy as np


def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))

learnrate = 0.5
x = np.array([1, 2])
y = np.array(0.5)

# Initial weights
weights = np.array([0.5, -0.5])

# Calculate one gradient descent step for each weight

# Calculate output of neural network
nn_output = sigmoid(np.dot(x, weights))

# Calculate error of neural network
# Where yHat = nn_output
error = y - nn_output


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

error_term = error * (sigmoid_prime(np.dot(x, weights)))

# Calculate change in weights
delta_w = [learnrate * error_term * x[0], learnrate * error_term * x[1]]

print('Neural Network output:')
print(nn_output)
print('Amount of Error:')
print(error)
print('Change in Weights:')
print(delta_w)
