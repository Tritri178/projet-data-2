import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Load the data

path='winemag-data-130k-v2.csv'

print('debug')
df = pd.read_csv(path)

print(df.keys())

# Extract X (price) and y (points)
X = df['price'].values
y = df['points'].values

# Remove any rows where price is NaN 
valid_indices = ~np.isnan(X) & ~np.isnan(y)
x = X[valid_indices]
y = y[valid_indices]

log_x = np.log(x)
coefficients = np.polyfit(log_x, y, 1) # returns [b, a]

b = coefficients[0]
a = coefficients[1]

y_fit = a + b * np.log(x)

# Plot the data and regression line
plt.scatter(x, y, color='blue', label='Data')
plt.scatter(x, y_fit, color='red', label='Regression Line')
plt.xlabel('Price ($)')
plt.ylabel('Points')
plt.title('Linear Regression: Points vs. Price')
plt.legend()
plt.show()

