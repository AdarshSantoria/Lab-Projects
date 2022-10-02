import numpy as np                 #importing required modules
import pandas as pd
import matplotlib.pyplot as plt
import math
'''1.'''
def pdf(x,lam):                    #defining PDF function using it's formula 
    return lam*math.exp(-lam*x)
def cdf(x,lam):                    #defining CDF function using it's formula 
    return 1-math.exp(-lam*x)
lam=57                             #given
x=np.arange(0,0.3,0.000001)        #taking some values of input in x
y=[]                               #making two lists y
for i in x:                        #running a for loop to append Values of PDF
    y.append(pdf(i,lam))           #for different values of x
#A
plt.plot(x,y)                      #plotting PDF
plt.show()
#B                                 #finding certain probilities using CDF values
print("Probability of wait time to be less than equal to 1 minutes",cdf(1/60,lam))
#C
print("Probability of wait time to be between 1 and 2 minutes",cdf(1/30,lam)-cdf(1/60,lam))
#D
print("Probability of wait time to be more than equal to 2 minutes",1-cdf(1/30,lam))
#E                                 #lamda value twices
print("Probability of wait time to be more than equal to 2 minutes",cdf(1/30,2*lam)-cdf(1/60,2*lam))
'''2'''
c=pd.read_csv("IC252_Lab7.csv")
#A                                 #codding entries of Status to some specific numbers
c['Status'] = c['Status'].replace('Hospitalized', 1)
c['Status'] = c['Status'].replace('Recovered', 2)
c['Status'] = c['Status'].replace('Dead', 3)
print(c['Status'])                 #printing status column
#B                                 
print("Correlation between Status & Population:",np.corrcoef(c['Status'],c['Population'])[1,0])
print("Correlation between Status & SexRatio:",np.corrcoef(c['Status'],c['SexRatio'])[1,0])
print("Correlation between Status & Literacy:",np.corrcoef(c['Status'],c['Literacy'])[1,0])
print("Correlation between Status & Age:",np.corrcoef(c['Status'],c['Age'])[1,0])
print("Correlation between Status & SmellTrend:",np.corrcoef(c['Status'],c['SmellTrend'])[1,0])
print("Correlation between Status & Gender:",np.corrcoef(c['Status'],c['Gender'])[1,0])
#C
print("As correlation between Status and Age is maximum, we can say Age is most strongly correlated")

               
