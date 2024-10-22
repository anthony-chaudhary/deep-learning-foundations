import numpy as np
from data_prep import features, targets, features_test, targets_test

np.random.seed(21)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Hyperparameters
n_hidden = 2  # number of hidden units
epochs = 900
learnrate = 0.005

n_records, n_features = features.shape
last_loss = None
# Initialize weights
weights_input_hidden = np.random.normal(scale=1 / n_features ** .5,
                                        size=(n_features, n_hidden))
weights_hidden_output = np.random.normal(scale=1 / n_features ** .5,
                                         size=n_hidden)

for e in range(epochs):
    del_w_input_hidden = np.zeros(weights_input_hidden.shape)
    del_w_hidden_output = np.zeros(weights_hidden_output.shape)
    for x, y in zip(features.values, targets):
        ## Forward pass ##
        # Calculate the output
        """
        This does the matrix multiplication of our 
        original data and our weights (where ever the weights happen to be at)
        """
        hidden_input = np.dot(x, weights_input_hidden)

        # the activation function that creates the non linearity in the model.
        hidden_output = sigmoid(hidden_input)

        """
        This is the second activation function that does the dot product on our
        hidden layer, and that layers weights, and then does the activation
        using sigmoid. This makes the network 2 layers deep
        """
        output = sigmoid(np.dot(hidden_output, weights_hidden_output))

        ## Backward pass ##

        # Calculate the error
        # Where y is the ground truth, and our output is the current rounds
        # guess at y
        error = y - output

        # Calculate error gradient in output unit
        # the slope of our error in respect to our output
        output_error = error * output * (1 - output)

        """
        The slope of the hidden error
        """
        # propagate errors to hidden layer
        hidden_error = np.dot(
            output_error, weights_hidden_output) * hidden_output * (1 - hidden_output)

        # Update the change in weights
        # Update the difference between the output error and the hidden output
        del_w_hidden_output += output_error * hidden_output
        del_w_input_hidden += hidden_error * x[:, None]

    # Update weights
    weights_input_hidden += learnrate * del_w_input_hidden / n_records
    weights_hidden_output += learnrate * del_w_hidden_output / n_records

    # Printing out the mean square error on the training set
    if e % (epochs / 10) == 0:
        hidden_output = sigmoid(np.dot(x, weights_input_hidden))
        out = sigmoid(np.dot(hidden_output,
                             weights_hidden_output))
        loss = np.mean((out - targets) ** 2)

        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss

# Calculate accuracy on test data
hidden = sigmoid(np.dot(features_test, weights_input_hidden))
out = sigmoid(np.dot(hidden, weights_hidden_output))
predictions = out > 0.5
accuracy = np.mean(predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))
