import numpy as np             #importing modules
import matplotlib.pyplot as plt
p = eval(input("Enter the prob of 1 :"))
#running 10000simulations
z = np.random.geometric(p, size=10000)
plt.hist(z)
#ploting of graph