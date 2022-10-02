# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:04:49 2022

@author: Adarsh
"""
#adding factorial formula
from math import factorial as fact      #fact(a) is factorial of a
'''
Ques 1
'''
N=int(input("founders:"))                     #N is number of founders
M=int(input("board positions:"))              #M is number of board positions
print("probability:", fact(N-M)/fact(N))
#formula of permutaion is used to assign M booard position to M person out of N
#and divide it by total permutaion of N persons for probaility
'''
Ques 2
'''
N=int(input("unique cards:"))                 #N is number of unique cards
D=int(input("cards in hand: "))               #D is number of cards in a hand
assert 6<=D<=8                                #D is from 6 to 8
#four 1s are choosen in a hand
print(fact(N-4)*fact(D)/(fact(D-4)*fact(N)))
#formula of combination is used to choose (D-4) cards from remaining (N-4)
#and divide it by total combination to choose  four cards from N to get probability
'''
Ques 3
'''
import random                                 #importing a module random
def dice(a):                                  #defining a function dice(a)
    count=0                                   #a is number of simulation
    for i in range(a):
        l=[1,2,3,4,5,6]                   #all entries of dice are listed as l
        o1=random.choice(l)               #variable is made to randomly choose a entry
        o2=random.choice(l)               #this is for two dices
        s= o1 + o2                        #s is their sum
        if(s%2!=0 or s>8):                #checking whether given condions are true
            count=count+1                 #if true, increase count(variable) by 1
    return count/a                        #returning probability using it's formula
print(dice(1000))                         #run the dice function for 1000simulation