import pandas as pd                       #importing modules
import numpy as np
import matplotlib.pyplot as plt
'''a'''
plt.rcParams["figure.figsize"]=(17,7)     #setting dimensions of plot graph
x=pd.read_csv('2021_IN_Region_Mobility_Report.csv')
x['date']=pd.to_datetime(x['date'])       #reading csv file and grouping dates to months
k=x[x['sub_region_1']=='Delhi']           #making two datset k & k1 to store inputs of Delhi and Mumbai respectively
k=k.groupby('date').mean()                #considering mean of datas of Delhi as it contains a large dataset
#plotting and labelling graph of Retail Mobility and Transit Mobility
plt.plot(k.index,k['retail_and_recreation_percent_change_from_baseline'],label='Delhi')
k1=x[x['sub_region_2']=='Mumbai']
plt.plot(k1['date'],k1['retail_and_recreation_percent_change_from_baseline'],label='Mumbai')
plt.legend()                              #showing labels on graph
plt.title('Retail mobility')              #titleing and naming the two axises
plt.xlabel('Dates')
plt.ylabel('retail_and_recreation_percent_change_from_baseline')
plt.show()
'''b'''
#plotting and labelling graph of Retail Mobility and Transit Mobility
plt.plot(k.index,k['transit_stations_percent_change_from_baseline'],label='Delhi')
plt.plot(k1['date'],k1['transit_stations_percent_change_from_baseline'],label='Mumbai')
plt.legend()                              #showing labels on graph
plt.title('Transit mobility')
plt.xlabel('Dates')              #titleing and naming the two axises
plt.ylabel('transit_stations_percent_change_from_baseline')
plt.show()
'''c'''
print('We can infer that the graph of Delhi is more diverse and values are generally greater than that of Mumbai')
'''d'''
#soring k and k2 to get 1st and 2nd half's median in order to get IQR through inbuilt formula
kk=k['retail_and_recreation_percent_change_from_baseline'].sort_values()
kk1=k1['retail_and_recreation_percent_change_from_baseline'].sort_values()
kk2=k['retail_and_recreation_percent_change_from_baseline'].sort_values()
kk3=k1['retail_and_recreation_percent_change_from_baseline'].sort_values()
print('IQR of Retail mobility of Delhi is',np.median(kk[(len(kk)//2)+1:])-np.median(kk[:len(kk)//2]))
print('IQR of Retail mobility of Mumbai is',np.median(kk1[(len(kk1)//2)+1:])-np.median(kk1[:len(kk1)//2]))
print('IQR of Transit mobility of Delhi is',np.median(kk2[(len(kk2)//2)+1:])-np.median(kk2[:len(kk2)//2]))
print('IQR of Transit mobility of Mumbai is',np.median(kk3[(len(kk3)//2)+1:])-np.median(kk3[:len(kk3)//2]))
'''e'''
#finding expected value by inbuilt formula of even
print('Expected Retail mobility of Delhi is',np.mean(k['retail_and_recreation_percent_change_from_baseline']))
print('Expected Retail mobility of Mumbai is',np.mean(k1['retail_and_recreation_percent_change_from_baseline']))
print('Expected Transit mobility of Delhi is',np.mean(k['transit_stations_percent_change_from_baseline']))
print('Expected Transit mobility of Mumbai is',np.mean(k1['transit_stations_percent_change_from_baseline']))