import numpy as np
import pandas as pd

df = pd.read_csv('../Brazil.csv').drop(['COUNTRY', 'PERWT'], axis=1)
df['constant'] = 1
df['female'] = (df['SEX'] == 'Female').astype(float)
df.drop('SEX', axis=1, inplace=True)

dummies = pd.get_dummies(df[['MARST', 'NATIVITY', 'EDATTAIN', 'EMPSTAT', 'OCCISCO', 'INDGEN']], drop_first=True).astype(np.int8)
df = pd.concat([df[['INCTOT']], dummies, df[['female', 'AGE', 'constant']]], axis=1)
df.to_csv('brazil_dummies.csv', index=False)