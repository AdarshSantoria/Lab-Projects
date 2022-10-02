from matplotlib import pyplot as plt
import random as r        #importing modules
C=[]                      
#C is a list that consists number of heads on simulating different times
N=int(input("number of indipendent throws:"))
p=float(input("probability of getting a Head:"))
S=[1]*int(100*N*p)+[0]*int(100*N*(1-p))   #adjusting probability of Head
for i in range(10000):                    #running 10000simulations
    x=[]
    for j in range(N):
        x.append(r.choice(S))
    C.append(x.count(1))
fig,ax = plt.subplots()          
#plotting the graph the results of all simuations
plt.title('Number of Heads obtained')
plt.xlabel('Favourable independent throws')
plt.ylabel('Number of heads')
ax.hist(C, bins=list(range(1, N+1)))

