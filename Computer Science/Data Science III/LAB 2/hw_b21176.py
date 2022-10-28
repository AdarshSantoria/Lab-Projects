import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math
plt.rcParams['figure.figsize'] = [12, 6]
x=pd.read_csv("landslide_data3_miss.csv")
x0=x
x1=pd.read_csv("landslide_data3_original.csv")
y=list(x.head())
y.pop(0)
y1=[]
for i in y:
    y1.append(x[i].isna().sum())
plt.plot(y,y1)
plt.title('Number of missing values')
plt.show()
x2=x.dropna(subset=['stationid'])
print(f'Total number of dropped rows having missing values for stationid is {len(x)-len(x2)}')
x=x2.dropna(thresh=len(y)/3)
print(f'Total number of dropped rows having missing values greater than one-third of attributes is {len(x2)-len(x)}')
for i in y:
    print(f'Number of missing values in attribute {i} is {x[i].isna().sum()}')
print(f'Total number of missing values is {x.isna().sum().sum()}')
y.pop(0)
y1=[]
for i in y:
    a=x0[i].fillna(np.mean(x[i]))
    print(f'replaced mean of attribute {i} is {np.mean(a)}')
    print(f'orignal mean of attribute {i} is {np.mean(x1[i])}')
    print(f'replaced median of attribute {i} is {np.median(a)}')
    print(f'orignal median of attribute {i} is {np.median(x1[i])}')
    print(f'replaced mode of attribute {i} is {statistics.mode(a)}')
    print(f'orignal mode of attribute {i} is {statistics.mode(x1[i])}')
    print(f'replaced standard deviation of attribute {i} is {np.std(a)}')
    print(f'orignal standard deviation of attribute {i} is {np.std(x1[i])}')
    y1.append(math.sqrt(np.square(np.subtract(x1[i],a)).mean()))
    print(f'RMSE of attribute {i} is {math.sqrt(np.square(np.subtract(x1[i],a)).mean())}') 
plt.plot(y,y1)
plt.title('RMSE b/w orignal and mean filled values')
plt.show()
y1=[]
for i in y:
    x0[i]=x0[i].interpolate()
    y1.append(math.sqrt(np.square(np.subtract(x1[i],x0[i])).mean()))
    print(f'RMSE of attribute {i} is {math.sqrt(np.square(np.subtract(x1[i],x0[i])).mean())}') 
plt.plot(y,y1)
plt.title('RMSE b/w orignal and interpolated values')
plt.show()
plt.boxplot(x0['temperature'])
plt.title('Interpolated Temperature')
plt.show()
plt.boxplot(x0['rain'])
plt.title('Interpolated Rain')
plt.show()
t=np.percentile(x0['temperature'] , [25 , 50 , 75])
ub=2.5*t[2] -1.5*t[0]
lb=2.5*t[0] -1.5*t[2]
x=x0['temperature']
b=np.median(x0['temperature'])
a=np.where((x<ub) & (x>lb),x,b)
plt.boxplot(a)
plt.title('outlier changed to Median')
plt.xlabel('Temperature')
plt.show()
t=np.percentile(x0['rain'] , [25 , 50 , 75])
ub=2.5*t[2] -1.5*t[0]
lb=2.5*t[0] -1.5*t[2]
x=x0['rain']
b=np.median(x)
a=np.where((x<ub) & (x>lb),x,b)
plt.title('outlier changed to Median')
plt.boxplot(a)
plt.xlabel('Rain')
plt.show()