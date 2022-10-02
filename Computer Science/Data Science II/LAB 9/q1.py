import matplotlib.pyplot as  plt           #importing modules
import numpy as np
from scipy.stats import bernoulli          #making list of different number of variables
m = [10, 100, 500, 1000, 5000, 10000, 50000]
'''a'''                                    
#Using inbuilt function to calculate mean of Exponential rv for different values of m
#by random values
v = [np.mean(np.random.exponential(1, i)) for i in m]
plt.plot(m, [1]*len(m), linestyle="--")
plt.plot(m, v)                             #plotting of graph and titling
plt.title("Exponential Distribution")
plt.show()

'''b'''
#Similarly for Uniform rv
v1 = [np.mean(np.random.uniform(1, 2, i)) for i in m]
plt.plot(m, [1.5]*len(m), linestyle="--")
plt.plot(m, v1)
plt.title("Uniform Distribution")
plt.show()

'''c'''
#Similarly for Bernoulli rv
v2 = [(sum(bernoulli.rvs(p=0.2, size=i))/len(bernoulli.rvs(p=0.2, size=i))) for i in m]
plt.plot(m, [0.2]*len(m), linestyle="--")
plt.plot(m, v2)
plt.title("Bernoulli Distribution")

