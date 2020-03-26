#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:52:42 2020

@author: ap
"""

import pandas as pd
import matplotlib.pyplot as plt
def biasPlot(x, y,kx = 10, ky = 10):
    if(len(x)!= len(y)):
        print("X,Y should be of equal length")
        return
    quantile_val_1 = [x.min()]
    quantile_val_2 = [y.min()]
    for i in range(1,kx+1):
        val = 1/kx*i
        quantile_val_1.append(x.quantile(val))
    for i in range(1,ky+1):
        val = 1/ky*i
        quantile_val_2.append(y.quantile(val))
    def range_val_return(num,arr):
        pos = 0;
        while(num>arr[pos]):
            pos = pos+1
        return pos
    
    for i in range(len(x)):
        x[i] = range_val_return(x[i],quantile_val_1)
        y[i] = range_val_return(y[i],quantile_val_2)
        
    For_plot2 = pd.DataFrame()
    For_plot2['one'] =[]
    For_plot2['two'] =[]
    For_plot2['value'] =[]
    k = 0;
    for i in range(1,kx+1):
        for j in range(1,ky+1):
            For_plot2.loc[k]=[i,j,0]
            k = k+1
    for i in range(len(x)):
        m_1 = x[i]
        m_2 = y[i]
        for i in range(len(For_plot2['one'])):
            if(m_1 == For_plot2['one'][i] and m_2 == For_plot2['two'][i] ):
                For_plot2['value'][i] = For_plot2['value'][i] +1

    plt.hist2d(For_plot2['one'], For_plot2['two'], weights=For_plot2['value'])      

cars_data = pd.read_csv('cars_sampled.csv')
cars = cars_data.copy()  
cars.drop_duplicates(keep = 'first',inplace = True)
cars = cars.dropna().reset_index(drop=True)           
cars.info()

biasPlot(cars['price'], cars['yearOfRegistration'])
plt.colorbar()
plt.xlabel("price(quantile)")
plt.ylabel("yearOfRegistration(quantile)")
plt.title("Bias Detection Plot")
plt.savefig("Bias_Detection_Plot_Price_year.pdf")
plt.savefig("Bias_Detection_Plot_Price_year.png")
plt.show()   


