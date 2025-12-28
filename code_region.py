import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def origine(path,country,province):
    path='data.csv'

    print('debug')
    df = pd.read_csv(path)

    print(df.keys())

    # Extract X (price) and y (points)
    x = df['price'].values
    y = df['points'].values
    countries = df['country'].values
    provinces = df['province'].values

    indice_1=countries==country
    indice_2=provinces==province


    # Remove any rows where price is NaN 
    valid_indices = ~np.isnan(x) & ~np.isnan(y) & indice_1 & indice_2
    x = x[valid_indices]
    y = y[valid_indices]
    countries = countries[valid_indices]
    provinces = provinces[valid_indices]

    return x, y, countries, provinces

x, y, countries, provinces = origine('data.csv','US','Oregon')



'''
log_x = np.log(x)
coefficients = np.polyfit(log_x, y, 1) # returns [b, a]

b = coefficients[0]
a = coefficients[1]

y_fit = a + b * np.log(x)

#%%

'''

# Plot the data and regression line
plt.scatter(x, y, color='blue', label='Data')
plt.xlabel('Price ($)')
plt.ylabel('Points')
plt.title('Linear Regression: Points vs. Price')
plt.xlim(left=0)   # set x-axis minimum to 0
plt.ylim(bottom=79) # set y-axis minimum to 0
plt.ylim(top=100)  # set y-axis maximum to 100
plt.legend()
plt.show()




# %%
