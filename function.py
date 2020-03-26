import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
def biasPlot(x, y,kx = 10, ky = 10 ,bins=10, range=None, density=False, weights=None, cmin=None, cmax=None, *, data=None, **kwargs):
	if(len(x)!= len(y)):
		print("X,Y should be of equal length")
		return
	quatile_val_1 = [x.min()]
	quatile_val_2 = [y.min()]
	for i in range(1,kx+1):
    val = 1/kx*i
    quatile_val_1.append(x.quantile(val))
  for i in range(1,ky+1):
    val = 1/ky*i
    quatile_val_2.append(y.quantile(val))
	def range_val_return(num,arr):
    pos = 0;
    while(num>arr[pos]):
        pos = pos +1;
    return pos
  for i in range(len(For_plot1['price'])):
    x[i] = range_val_return(x[i],quatile_val_1)
    y[i] = range_val_return(y[i],quatile_val_2)  
  
  For_plot2 = pd.DataFrame()
	For_plot2['one'] =[]
	For_plot2['two'] =[]
	For_plot2['value'] =[]
	k = 0;
	for i in range(1,k1+1):
	    for j in range(1,k2+1):
	        For_plot2.loc[k]=[i,j,0]
	        k = k +1 
	for i in range(len(x)):
		m_1 = x[i]
		m_2 = y[i]
    for i in range(len(For_plot2['one'])):
        if(m_1 == For_plot2['one'][i] and m_2 == For_plot2['two'][i] ):
            For_plot2['value'][i] = For_plot2['value'][i] +1
  plt.hist2d(For_plot2['one'], For_plot2['two'], weights=For_plot2['value'],
  						bins=bins, range=range, density=density, cmin=cmin, cmax=cmax, *, **kwargs)          