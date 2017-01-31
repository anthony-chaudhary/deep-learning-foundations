import pandas as pd
from sklearn import linear_model, metrics
import matplotlib.pyplot as plt

# read data
dataframe = pd.read_csv('challenge_dataset.csv')
x_values = dataframe[[1]]
y_values = dataframe[[0]]

# train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)


# Score
x = metrics.mean_squared_error(y_values, body_reg.predict(x_values))
print(x)


# visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
