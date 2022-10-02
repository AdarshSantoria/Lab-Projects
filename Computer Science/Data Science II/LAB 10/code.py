import numpy as np                #importing numpy module
'''a'''
n=[100,1000,10000]                #makinging a list of given sample sizes
for i in n:                       #running a loop for given sample sizes
    c=0                           #making a variables and add 1 if favourable
    for j in range(i):            #running a loop for given sample sizes
        x=np.random.uniform(-1,1) #making a random 2-d co-ordinate (x,y) where
        y=np.random.uniform(-1,1) # -1>=x>=1 & -1>=x>=1
        o=(x**2 +y**2)**(0.5)     # o is distance from origin
        if o<=1:                  # if o<=1, it is a favourable case
            c+=1
    print('Pi =',round(4*c/i,3),'for',i,'simulations')
#Pi is approximated using Monte Carlo
'''b'''
for i in n:                       #running a loop for given sample sizes
    f=0                           
#making a variable and adding value of different points on function with respect to x
    for j in range(i):            #running a loop for given sample sizes
        x=np.random.uniform(0,1)  #making a variable x to store a random number between 0 & 1
        f+=2/(1+x**2)
    print('Integral =',round(f/i,3),'for',i,'simulations')           
#integral of function is approximated using Monte Carlo
'''c'''
for i in n:                       #running a loop for given sample sizes
    c=0                           #making a variable c
    l=np.arange(1,i+1)            #making a list containing all values from 1 to given sample sizes 
    for j in range(10000):        #running 10000 simulations
        np.random.shuffle(l)      #randomly shuffling list l
        for k in range(i):        #running for loop in l
            if l[k]==k+1:
                c+=1              #counting number of favourable cases in c
                break
    print('e =',10000/(10000-c),'for',i,'simulations')       
#e is approximated using Monte Carlo
            
    