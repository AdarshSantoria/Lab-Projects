import numpy as np                      #importing modules
from scipy.stats import bernoulli, norm
import matplotlib.pyplot as plt
from statistics import stdev
n = [1, 2, 4, 8, 16, 32]                #making list of different number of variables
exp = []
uni = []
ber = []
for i in n:
    e = np.zeros(1000)
    u = np.zeros(1000)
    b = np.zeros(1000)
    for j in range(i):                  #using inbuilt formula to calculate mean of all type sof variables
        e += np.random.exponential(1, 1000)/i
        u += np.random.uniform(1, 2, 1000)/i
        b += bernoulli.rvs(p=0.2, size=1000)/i
    exp.append(e)                       #filling the values of different rvs in different lists
    uni.append(u)
    ber.append(b)
f = [exp, uni, ber]                     #making a nested list of types of variables
fig, axs = plt.subplots(3, 6, figsize=(24, 12))
c= ["n = " + str(i) for i in n]
r= ["EXPONENTIAL", "UNIFORM", "BERNOULLI"]    #making a list of titles used to tiltle during for loop
for i in range(6):
    axs[0, i].set_title(c[i])            #tiltling of all types of graphs
for i in range(3):
    axs[i, 0].set_ylabel(r[i])
    if i == 0:
        vals = 100
    if i == 2 :
        vals = 10
    for j in range(6):                   #Plotting of histogram for different graphs
        count, bins, ignored = axs[i, j].hist(
            f[i][j], vals, density=True)
        axs[i, j].plot(bins, norm.pdf(bins, loc=np.mean(f[i][j]),
                                      scale=stdev(f[i][j])))
plt.show()