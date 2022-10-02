import pandas as pd
import numpy as np
X=[15,17,20,21,25]
Y=[9,13,16,18,21]
n=len(X)
EX=sum(X)/n
EY=sum(Y)/n
xy=0
x=0
y=0
for i in range(n):
    xy+=(X[i]-EX)*(Y[i]-EY)
    x+=(X[i]-EX)**2
    y+=(Y[i]-EY)**2
'''a'''
print('a.')
print("COV(X,Y)=",xy/(n-1))
print("Using numpy COV(X,Y)=",np.cov(X,Y)[0,1])
'''b'''
print('b.')
print("COR(X,Y)=",xy/((x*y)**(0.5)))
print("Using numpy COR(X,Y)=",np.corrcoef(X,Y)[0,1])
'''c'''
print('c.')
x=pd.read_csv("BNG-Device_Lab6.csv")
x=x.dropna()
print("COR(Active-Count,CPU-Utilization)=",np.corrcoef(x["Active-Count"],x["CPU-Utilization"])[0,1])
print("COR(CPU-Utilization,Total-Memory-Usage)=",np.corrcoef(x["CPU-Utilization"],x["Total-Memory-Usage"])[0,1])
print("COR(CPU-Utilization,Average-Temperature)=",np.corrcoef(x["CPU-Utilization"],x["Average-Temperature"])[0,1])
print("COR(Active-Count,Average-Temperature)=",np.corrcoef(x["Active-Count"],x["Average-Temperature"])[0,1])
print("COR(Total-Memory-Usage,Average-Temperature)=",np.corrcoef(x["Total-Memory-Usage"],x["Average-Temperature"])[0,1])