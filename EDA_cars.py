# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:29:29 2020

@author: Antonin

Exploratory Data Analysis of DataSet Cars
from Coursera, module 6 Data Analysis with Python
week 3
"""

import pandas as pd
import numpy as np

path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
print(df.dtypes)

df.corr()
pd.set_option('display.max_columns', 100)

df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()

sns.regplot(x ='engine-size', y = 'price', data = df)
plt.ylim(0,)
df[['engine-size', 'price']].corr()

sns.regplot( x='highway-mpg', y='price', data=df)
df[['highway-mpg', 'price']].corr()

sns.regplot(x='peak-rpm', y='price', data=df)
df[['peak-rpm', 'price']].corr()

sns.regplot( x='stroke', y = 'price', data = df )
df[['stroke', 'price']].corr()

sns.boxplot(x = 'body-style', y = 'price', data = df)
sns.boxplot( x = 'engine-location', y = 'price', data = df)
sns.boxplot(x= 'drive-wheels', y='price', data = df)

df.describe()
df.describe(include=['object'])

df['drive-wheels'].value_counts()
df['drive-wheels'].value_counts().to_frame()

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns = {'drive-wheels': 'value_counts'}, inplace = True)

drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts

engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)

df['drive-wheels'].unique()

df_group_one = df[['drive-wheels', 'body-style', 'price']]
df_group_one = df_group_one.groupby(['drive-wheels'], as_index=False).mean()
df_group_one

df_gptest = df[['drive-wheels', 'body-style', 'price']]
grouped_test1 = df_gptest.groupby(['drive-wheels', 'body-style'], as_index = False).mean()
grouped_test1

grouped_pivot = grouped_test1.pivot(index = 'drive-wheels', columns ='body-style')
grouped_pivot

grouped_pivot = grouped_pivot.fillna(0)
grouped_pivot

df_group_one = df[['drive-wheels', 'body-style', 'price']]
df_group_one_B = df_group_one.groupby(['body-style'], as_index=False).mean()
df_group_one_B

plt.pcolor(grouped_pivot, cmap ='RdBu')
plt.colorbar()
plt.show()


fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap= 'RdBu')

row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor = False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor = False)

ax.set_xticklabels(row_labels, minor = False)
ax.set_yticklabels(col_labels, minor = False)

plt.xticsk(rotation = 90)

fig.colorbar(im)
plt.show()

pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print('The Pearson Correlation Coefficient is', pearson_coef, 'with a P-value of P =', p_value)

pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)

pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value ) 

pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  

pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value) 

pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value ) 

pearson_coef, p_value = stats.pearsonr(df['city-mpg'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  

pearson_coef, p_value = stats.pearsonr(df['highway-mpg'], df['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value ) 

grouped_test2 = df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(5)

df_gptest

grouped_test2.get_group('4wd')['price']

#ANOVA
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'], grouped_test2.get_group('4wd')['price'])
print('ANOVA results: F=', f_val, ' P= ', p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val )

f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])  
   
print( "ANOVA results: F=", f_val, ", P =", p_val) 

f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])  
 
print("ANOVA results: F=", f_val, ", P =", p_val)   

