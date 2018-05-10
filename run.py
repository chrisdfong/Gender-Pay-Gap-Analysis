import numpy as np
import pandas as pd
import statsmodels.api as sm

two_rows = []
three_rows = []

for cntry in ['Canada', 'Panama', 'PuertoRico', 'UnitedStates']:
    single_two = [cntry]
    single_three = [cntry]
    
    df = pd.read_csv('../'+cntry +'.csv').drop(['COUNTRY', 'PERWT'], axis=1)
    df['constant'] = 1
    df['female'] = (df['SEX'] == 'Female').astype(float)
    df.drop('SEX', axis=1, inplace=True)
    
    dummies = pd.get_dummies(df[['MARST', 'NATIVITY', 'EDATTAIN', 'EMPSTAT', 'OCCISCO', 'INDGEN']], drop_first=True).astype(np.int8)
    df = pd.concat([df[['INCTOT']], dummies, df[['female', 'AGE', 'constant']]], axis=1)
    
    male = df[df['female']==0].reset_index(drop=True).drop('female', axis=1)
    female = df[df['female']==1].reset_index(drop=True).drop('female', axis=1)

    Xm = male.drop('INCTOT', axis=1)
    Xf = female.drop('INCTOT', axis=1)
    Ym = male['INCTOT']
    Yf = female['INCTOT']
    
    female_model = sm.OLS(Yf, Xf).fit()
    male_model = sm.OLS(Ym, Xm).fit()
    
    Bf = female_model.params
    Bm = male_model.params
    
    male_mean = np.mean(Ym)
    female_mean = np.mean(Yf)
    
    single_two.append(male_mean)
    single_three.append(male_mean)
    
    single_two.append(female_mean)
    single_three.append(female_mean)

    gap = male_mean - female_mean
    
    single_two.append(gap)
    single_three.append(gap)
    
    endowments = np.transpose(np.mean(Xm) - np.mean(Xf)) @ np.array(Bf)
    coefficients = np.transpose(np.mean(Xf)) @ np.array(Bm - Bf)
    interaction = np.transpose(np.mean(Xm) - np.mean(Xf)) @ np.array(Bm - Bf)
    
    single_three.append(endowments)
    single_three.append(coefficients)
    single_three.append(interaction)
    
    pooled_model = sm.OLS(df['INCTOT'], df.drop('INCTOT', axis=1)).fit()
    B_star = pooled_model.params.drop('female')
    
    explained = np.transpose(np.mean(Xm) - np.mean(Xf)) @ np.array(B_star)
    unexplained = np.transpose(np.mean(Xm)) @ np.array(Bm-B_star) + np.transpose(np.mean(Xf)) @ np.array(B_star-Bf)
    
    single_two.append(explained)
    single_two.append(unexplained)

    two_rows.append(single_two)
    three_rows.append(single_three)
    
two = pd.DataFrame(two_rows, columns=['Country', 'Group 1', 'Group 2', 'Gap', 'Explained', 'Unexplained'])
three = pd.DataFrame(three_rows, columns=['Country', 'Group 1', 'Group 2', 'Gap', 'Endowments', 'Coefficients', 'Interaction'])

two.to_csv('two_fold.csv', index=False)
three.to_csv('three_fold.csv', index=False)