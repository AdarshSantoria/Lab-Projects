import random as r                    #importing modules
from collections import Counter
import matplotlib.pyplot as plt
'''a'''
def cVsn(d,n):                        #making a function to make graph
    N=[]                              #making a list N and adding no. of 
    c=[]                              #days in a year with the help of loop
    for i in range(1,n+1):            #c is a list containg favorable outcomes
        days=[]                       #from list days containing all random bdays
        N.append(i)
        for j in range(i):            #simulating i times
            days.append(r.randint(1,d))
        days=Counter(days)
        count=0
        for j in days.values():       #checking favourable condition
            if(j>1):
                count+=j
        c.append(count)
    plt.plot(N,c)                     #plotting of graph
    plt.xlabel("n")
    plt.ylabel("c")
    plt.show()
n=int(input("no. of people:"))        #applying for 365 days
cVsn(365,n)
'''b'''
n=int(input("no. of people:"))        #applying for 687 days
cVsn(687,n)
'''c'''
c=0                                   #initialise c from 0
n=int(input("no. of people:"))
for i in range(1000):                 #run 1000simulations
    days=[]                           #running similar operation as before
    for j in range(n):
        days.append(r.randint(1, 365))
    x=Counter(days)
    count=0
    for i in x.values():              #if random case is true add 1 to count
        if(i>1):
            count+=i
    if(count>1):
        c+=1                          #calculate no. of favourable case (c)
print("Average probabilty that c is atleast 2 is",(c/1000))
#probability is printed with the help of it's formula
'''d'''
N=[]
c=[]                                 #similar operations are performed as in a
arr=[]
for i in range(1,367):
    N.append(i)                      #but probability of days between 1 and 150
    if(i<151):                       #are twice  as compared to between 151 and 365
        arr.append(i)                #as arr conatains the prior souble
        arr.append(i)
    else:
        arr.append(i)
for n in range(1,367):
    days=[]
    for i in range(n):
        days.append(r.choice(arr))
    x=Counter(days)
    count=0
    for i in x.values():
        if(i>1):
            count=count+i
    c.append(count)                  #plotting of graph
plt.plot(N,c)
plt.xlabel("n")
plt.ylabel("c") 