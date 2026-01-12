import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
csv_file='data.csv'
data=pd.read_csv(csv_file)

def nettoyage_donnees(data):


    

    x = data['price'].values
    y = data['points'].values

    print('Avant le nettoyage de donnees nous avons', len(x), 'elements')

    valid_indices = ~np.isnan(x) & ~np.isnan(y)
    x = x[valid_indices]
    y = y[valid_indices]

    print('apres le nettoyage de donnees nous avons', len(x), 'elements')

    return x, y
