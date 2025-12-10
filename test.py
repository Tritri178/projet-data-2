import numpy as np
from scipy import stats


data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)

 

'''
lope, intercept, r_value, p_value, std_err = stats.linregress(X, y)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")

y_pred = intercept + slope * X

print("\nPredicted values:")
print(y_pred)

'''