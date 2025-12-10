import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Load the data

path='/Users/meljansevanrensburg/Desktop/3GM/DATA/Projet/winemag-data_first150k.csv'

df = pd.read_csv(path)

# Extract X (price) and y (points)
X = df['price'].values
y = df['points'].values

# Remove any rows where price is NaN (if any)
valid_indices = ~np.isnan(X) & ~np.isnan(y)
X = X[valid_indices]
y = y[valid_indices]

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(X, y)

# Print the results
print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_value**2:.4f}")

# Predict y values using the regression line
y_pred = intercept + slope * X

# Plot the data and regression line
plt.scatter(X, y, color='blue', label='Data')
plt.xlabel('Price ($)')
plt.ylabel('Points')
plt.title('Linear Regression: Points vs. Price')
plt.legend()
plt.show()
