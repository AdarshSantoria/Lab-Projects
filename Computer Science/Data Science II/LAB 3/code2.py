# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:07:49 2022

@author: HP
"""
import matplotlib.pyplot as plt        #importing required modules
from random import randint as r
def die2BiasedCoin(N):                 #making a function
    H=0                                #make variable H & T to respectively
    T=0                                #initialise number of heads and tails from 0
    for i in range(N):                 #run a loop for number of throws
        n=r(1,6)                       #randomly take any number from 1 to 6 as in die
        if (n == 2) or (n == 3):       #taking a biased situation where 2 out of 6 cause Head
            H = H+1                    #H or T based on situation by 1
        else:
            T=T+1
    print("Head occurs ",H,"times")    #printing total no. of H & T
    print("Tail occurs ",T,"times") 
    #Ploting the bar graph
    plt.bar(["Heads","Tails"],[H,T])
    plt.xlabel("Outcomes")             #labelling the graph
N=int(input("no. of times to repeat:"))
die2BiasedCoin(N)
