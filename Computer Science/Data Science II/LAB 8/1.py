import pandas as pd                       #importing modules
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"]=(17,7)     #setting dimensions of plot graph
x=pd.read_csv('cases.csv')                #reading csv file and grouping dates to months
x['Date']=pd.to_datetime(x['Date'])
k=x[x['State']=='Delhi']                  #making two datset k, k1 & k2 to store inputs of Delhi, Kolkata and Mumbai respectively
k['Infected Fraction']=(k['Confirmed']-k['Recovered'] -k['Deceased'])/20591874
plt.plot(k['Date'],k['Infected Fraction'],label='Delhi') #plotting graph
k2=x[x['District']=='Mumbai']
k2['Infected Fraction']=(k2['Confirmed']-k2['Recovered'] -k2['Deceased'])/20667656
plt.plot(k2['Date'],k2['Infected Fraction'],label='Mumbai')
k1=x[x['District']=='Kolkata']
k1['Infected Fraction']=(k1['Confirmed']-k1['Recovered'] -k1['Deceased'])/14850000
plt.plot(k1['Date'],k1['Infected Fraction'],label='Kolkata')
plt.legend()                              #showing labels on graph
plt.title('Time Graph')                   #titleing and naming the two axises
plt.xlabel('Time in Months')
plt.ylabel('Infected Fraction')
plt.show()                                #finding variance of found infected column
l=[k['Infected Fraction']]
l1=[k1['Infected Fraction']]
l2=[k2['Infected Fraction']]
print('Variance of infected person is: ',np.var(l+l1+l2))