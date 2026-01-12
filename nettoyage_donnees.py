import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
csv_file='data.csv'
data=pd.read_csv(csv_file)

import pandas as pd
import numpy as np

def nettoyage_et_export(csv_file, output_file):

    data = pd.read_csv(csv_file)
    print(f"Avant le nettoyage : {len(data)} éléments")

 
    data_clean = data.dropna(subset=['price', 'points'])
    data_clean = data_clean[data_clean['price'] > 0]

    print(f"Après le nettoyage : {len(data_clean)} éléments")

    data_clean.to_csv(output_file, index=False)
    print(f"Nouveau jeu de données sauvegardé sous : {output_file}")
    
    return data_clean

csv_file = 'data.csv'
data_cleaned = nettoyage_et_export(csv_file, 'data_cleaned.csv')

def nettoyage_donnees(data):


    

    x = data['price'].values
    y = data['points'].values

    print('Avant le nettoyage de donnees nous avons', len(x), 'elements')

    valid_indices = ~np.isnan(x) & ~np.isnan(y)
    x = x[valid_indices]
    y = y[valid_indices]

    print('apres le nettoyage de donnees nous avons', len(x), 'elements')

    return x, y
