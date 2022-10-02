# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 01:01:14 2022

@author: HP
"""
import random as r                    #importing modules
from collections import Counter
import matplotlib.pyplot as plt
def bday(n,d):                        #making a function
    N=[]                              #making a list N and adding no. of 
    c=[]                              #days in a year with the help of loop
    for i in range(1,n+1):            #c is a list containg favorable outcomes
        N.append(i)
        t=0
        for k in range(1000):         #running 1000 simulations
            days=[]      
            count=False
            for j in range(1,i+1):            
                days.append(r.randint(1,d))          
            da=Counter(days)          #randomly taking a day 
            for j in da.values():     #checking favourable condition
                if(j>1):
                    count=True
                    break
            if count:                 #counting no. of favourable cases
                t+=1
        c.append(t/1000)              #appending probability to the list
    plt.plot(N,c)                     #plotting of graph
    plt.xlabel("n")
    plt.ylabel("c")
    plt.show()
'''a'''
bday(100,365)                         #100 people in 365 days pf year
'''b'''
bday(100,669)                         #100 people in 669 days of year
'''c'''
N=[]                                  #making a list N and adding no. of 
c=[]
arr=[]                               #n is number of people
n=int(input("number of people:"))    #similar operations are performed
for i in range(1,n+1):               #but probability of days between 1 and 150
    if(i<151):                       #are twice  as compared to between 151 and 365
        arr.append(i)                #as arr conatains the prior double
        arr.append(i)
    else:
        arr.append(i)                #days in a year with the help of loop
for i in range(1,n+1):               #c is a list containg favorable outcomes
    N.append(i)
    t=0
    for k in range(1000):         #running 1000 simulations
        days=[]      
        count=False
        for j in range(1,i+1):            
            days.append(r.choice(arr))          
        da=Counter(days)          #randomly taking a day 
        for j in da.values():     #checking favourable condition
            if(j>1):
                count=True
                break
        if count:                 #counting no. of favourable cases
            t+=1
    c.append(t/1000)              #appending probability to the list
plt.plot(N,c)                     #plotting of graph
plt.xlabel("n")
plt.ylabel("c")
plt.show()

