# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 01:09:54 2020

@author: Abhinandan Pal
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

cars_data = pd.read_csv('cars_sampled.csv')
cars = cars_data.copy()
cars['yearOfRegistration'].describe()
cars.drop_duplicates(keep = 'first',inplace = True)

For_plot1 = pd.DataFrame()

For_plot1['price'] = cars['price']
For_plot1['yearOfRegistration'] = cars['yearOfRegistration']
For_plot1 = For_plot1.dropna().reset_index(drop=True)
For_plot1.describe()
k1 = 10
k2 = 8
quatile_val_1 = [For_plot1['price'].min()]
quatile_val_2 = [For_plot1['yearOfRegistration'].min()]

for i in range(1,k1+1):
    val = 1/k1*i
    quatile_val_1.append(For_plot1['price'].quantile(val))
 
for i in range(1,k2+1):
    val = 1/k2*i
    quatile_val_2.append(For_plot1['yearOfRegistration'].quantile(val))

range_val_1 = []
range_val_2 = []

def range_val_return(num,arr):
    pos = 0;
    while(num>arr[pos]):
        pos = pos +1;
    return pos

for i in range(len(For_plot1['price'])):
    range_val_1.append(range_val_return(For_plot1['price'][i],quatile_val_1))
    range_val_2.append(range_val_return(For_plot1['yearOfRegistration'][i],quatile_val_2))
    

For_plot1['price'] = range_val_1
For_plot1['yearOfRegistration'] = range_val_2    

For_plot2 = pd.DataFrame()

For_plot2['one'] =[]
For_plot2['two'] =[]
For_plot2['value'] =[]
k = 0;
for i in range(1,k1+1):
    for j in range(1,k2+1):
        For_plot2.loc[k]=[i,j,0]
        k = k +1
        
def increase(m_1,m_2):
    for i in range(len(For_plot2['one'])):
        if(m_1 == For_plot2['one'][i] and m_2 == For_plot2['two'][i] ):
            For_plot2['value'][i] = For_plot2['value'][i] +1
            
for i in range(len(For_plot1['price'])):
    increase(For_plot1['price'][i],For_plot1['yearOfRegistration'][i])
    
plt.hist2d(For_plot2['one'], For_plot2['two'], weights=For_plot2['value'])    
plt.colorbar()
plt.show()            
        
