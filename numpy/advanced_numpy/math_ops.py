# Numpy allows easy creation of loss functions

import numpy as np

# Sigmoid: It takes any real number (from −∞ to +∞) and squashes it into range (0,1)


def sigmoid(arr):
    return 1 / (1 + np.exp(-(arr)))


a = np.arange(100)
print(f"{sigmoid(a)}\n")

# Mean Squared Error (MSE) :Its a metric that quantifies the average squared difference between a model's predicted values and the actual values in a dataset

actual = np.random.randint(1, 50, 25)
predicted = np.random.randint(1, 50, 25)


def mean_squared_error(actual_arr, predicted_arr):

    return np.mean((actual_arr - predicted_arr) ** 2)


print(f"Actual\n{actual}\n")
print(f"Predicted\n{predicted}\n")
print(f"Mean squared Error: {mean_squared_error(actual, predicted)}\n")


def binary_cross_entropy(y_true, y_pred):
    # Adding epsilon to avoid log(0)
    eps = 1e-15
    y_pred = np.clip(y_pred, eps, 1 - eps)

    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))


y_true = np.array([1, 0, 1, 0])
logits = np.array([2.0, -1.0, 3.0, -2.0])
y_pred = sigmoid(logits)

print("Predicted probabilities:", y_pred)
print("BCE Loss:", binary_cross_entropy(y_true, y_pred))
