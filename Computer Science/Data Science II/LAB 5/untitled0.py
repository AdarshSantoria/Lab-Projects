'''a'''
import random as r                    #importing modules
import matplotlib.pyplot as plt
I=[]
N=10000                              #N is number of simulations
for i in range (N):
    I.append(r.randint(0,1))         #randomly taking values for X
print("P(X=0)=",I.count(0)/N)        
print("P(X=1)=",I.count(1)/N)
O=[]
x=int(0.25*100)*[1]+int(0.75*100)*[0] #setting probability for 0 & 1 in Y
y=int(0.65*100)*[1]+int(0.35*100)*[0]
for i in I:
   if(i==0):
       O.append(r.choice(x))
   elif(i==1):
       O.append(r.choice(y))
y0=O.count(0)/N 
y1=O.count(1)/N 
print("P(Y=0)=",y0)
print("P(Y=1)=",y1)
yvalues = ['0','1']            #plotting of graph
prob= [y0,y1]
plt.bar(yvalues,prob)
plt.xlabel("Values of Y")
plt.ylabel("Probability")
plt.title("Distribution of Y")
plt.show()
'''b'''
a=0
b=0
c=0
d=0
for i in range(10000):          #finding requiured outputs
    if(I[i]==O[i]==0):
        a=a+1
    elif(I[i]==O[i]==1):
        b=b+1
    elif(I[i]==0) and (O[i]==1):
        c=c+1
    elif(I[i]==1) and (O[i]==0):
        d=d+1
y0x0=a/I.count(0)
y1x1=b/I.count(1)
y1x0=c/I.count(0)
y0x1=d/I.count(1)
print("Verifying equations of 'a' part")
print("P(Y=0",y0x0*I.count(0)/N+y0x1*I.count(1)/N)
print("P(Y=1",y1x0*I.count(0)/N+y1x1*I.count(1)/N)
print("P(Y=0|X=0)=",y0x0)
print("P(Y=1|X=1)=",y1x1)
print("P(Y=1|X=0)=",y1x0)
print("P(Y=0|X=1)=",y0x1)            #plotting of graph
yval = ['Y=0,X=0' ,'Y=1,X=1' ,'Y=1,X=0' ,'Y=0,X=1']
prob= [a,b,c,d]
plt.bar(yval,prob)
plt.xlabel("XY")
plt.ylabel("Outcomes")
plt.title("Joint distribution of XY")
