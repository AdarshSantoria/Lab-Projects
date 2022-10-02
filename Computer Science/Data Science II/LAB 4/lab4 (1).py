from random import randint as r #importing modules
Z=[]                            #making lists and appending random values
X1=[]                           #with the help of for loop
X2=[]                           #N is number simulations
N=int(input("number of times the loop needs to run:"))
for i in range(N):
    X1.append(r(0,1))
    X2.append(r(0,1))
    Z.append(X1[-1]+X2[-1])     #Z is sum of outcome of X1 & X2
'''a'''                         #desired probabilities are obtained by using 
print("P((X1=1 AND X2=1)):",Z.count(2)/N)     #probability formula
print("P(X1=1)",X1.count(1)/N)
print("P(X2=1)",X2.count(1)/N)
'''b'''                         #checking Z is independent of X1 or not
print("P(X1=1)*P(Z=1):",(X1.count(1)/N)*(Z.count(1)/N))
count=0
for i in range(N):              #taking one case when X1=Z=1
    if X1[i]==1 and Z[i]==1:
        count+=1
print("P(X1=1 AND Z=1):",count/N)   #There is a mismatch
print("Hence,Z is not independent of X1")
'''c'''
c1=0                           #outcomes are counted inside samplespace
c2=0                           #when Z is 1
c3=0
for i in range(N):
    if(X1[i]==1) and (X2[i]==1) and (Z[i]==1):
        c1=c1+1
    if(X1[i]==1) and (Z[i]==1):
        c2=c2+1
    if(X2[i]==1) and (Z[i]==1):
        c3=c3+1
print("P(X1=1,X2=1 | Z=1):",c1/Z.count(1))
print("P(X1=1 | Z=1)*P(X2=1 | Z=1):",(c2/Z.count(1))*(c3/Z.count(1)))
print("Hence,X1 & X2 are not independent under condition of Z")
