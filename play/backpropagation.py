import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.array([0.5, 0.1, -0.2])
target = 0.6
learnrate = 0.5

weights_input_hidden = np.array([[0.5, -0.6],
                                 [0.1, -0.2],
                                 [0.1, 0.7]])

weights_hidden_output = np.array([0.1, -0.3])

# Forward pass
hidden_layer_input = np.dot(x, weights_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)

output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)
output = sigmoid(output_layer_in)

# Backwards pass
# Calculate error
error = target - output
print("Error: ", error)

# Calculate error gradient for output layer
delta_err_output = error * output * (1 - output)
print("delta error output:", delta_err_output)

# Calculate error gradient for hidden layer
delta_err_hidden = np.dot(delta_err_output, weights_hidden_output) * \
    hidden_layer_output * (1 - hidden_layer_output)
print("delta error hidden:", delta_err_hidden, "\n")

# Calculate change in weights for hidden layer to output layer
delta_weights_hidden_output = learnrate * \
    delta_err_output * hidden_layer_output

# Calculate change in weights for input layer to hidden layer
delta_weights_input_to_hidden = learnrate * delta_err_hidden * x[:, None]

print('Change in weights for hidden layer to output layer:')
print(delta_weights_hidden_output)
print('Change in weights for input layer to hidden layer:')
print(delta_weights_input_to_hidden)
