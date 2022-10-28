# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:37:17 2022

@author: Adars
"""
import numpy as np                 #importing modules
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance
import statistics as st
import copy
from numpy.core.fromnumeric import var
from sklearn.decomposition import PCA
'''1'''
x=pd.read_csv('pima-indians-diabetes.csv')   #reading csv file
x0=pd.read_csv('pima-indians-diabetes.csv')
y=list(x.head())
y.pop()
for i in y:
    a=np.quantile(x[i],[0.25,0.5,0.75])     #making a list containg values of 1st,2nd & 3rd quantile
    ub=2.5*a[2]-1.5*a[0]                    #ub and lb
    lb=2.5*a[0]-1.5*a[2]
    x[i]=np.where((x[i]>ub) | (x[i]<lb),a[1],x[i]) # replacing outliers with median
    x0[i]=np.where((x0[i]>ub) | (x0[i]<lb),a[1],x0[i])
for i in y:
    mx=np.max(x[i])                         #finding max & min value
    mn=np.min(x[i])
    print(f'min value of {i} before min-max normalisation is {mn}')
    print(f'max value of {i} before min-max normalisation is {mx}')
    x[i]=np.where(True,5+ 7*(mx-x[i])/(mx-mn),0)  #normalise data with range 5-12
    mx=np.max(x[i])
    mn=np.min(x[i])
    print(f'min value of {i} after min-max normalisation is {mn}')
    print(f'max value of {i} after min-max normalisation is {mx}')
for i in y:
    mean=np.mean(x0[i])                      #finding min & max value
    std=np.std(x0[i])
    print(f'mean of {i} before standardization is {mean}')
    print(f'standard deviation of {i} before standardization is {std}')
    x[i]=np.where(True,(x0[i]-mean)/std,0)   #fitting equation as described in ques
    mean=np.mean(x0[i])
    std=np.std(x0[i])
    print(f'mean of {i} after standardization is {mean}')
    print(f'standard deviation of {i} after standardization  is {std}')
'''2'''
mean =[0, 0]                                 #given mean and covariance matrix
cm = [[13, -3], [-3, 5]]
ds = np.random.multivariate_normal(mean, cm, 1000) #randomly operate one normalised data
plt.scatter(ds[:,0],ds[:,1])                       #plotting scatter plot
plt.title('Scatter Plot of Data Samples')
eigval, eigvec = np.linalg.eig(cm)                 #finding eigen vector and value
print("Eigvalues are", eigval)
v1 = eigvec[:, 0]
v2 = eigvec[:, 1]
print("Eigvectors are", v1, "and", v2)
plt.quiver(0,0, v1[0], v1[1], label='v1',color='red') #plotting eigen directions and lengend them
plt.quiver(0,0,v2[0], v2[1],label='v2',color='yellow')
plt.legend()
plt.show()
m1 = np.matmul(v1.T, ds.T)                       #matrix multiplication of vector with sample data
m2 = np.matmul(v2.T, ds.T)
pro1 = [[], []]
pro2 = [[], []]
for i in range(m1.size):
    s = m1[i]*v1.T
    t = m2[i]*v2.T
    pro1[0].append(s[0])
    pro1[1].append(s[1])
    pro2[0].append(t[0])
    pro2[1].append(t[1])
plt.scatter(ds[:,0],ds[:,1])
plt.scatter(pro1[0], pro1[1],color='green')
plt.show()
plt.scatter(ds[:,0],ds[:,1])
plt.scatter(pro2[0], pro2[1],color='green')
plt.show()
data = pd.DataFrame()
for i in range(1000):
    newvec = m1[i]*v1 + m2[i]*v2
    data.loc[i] = newvec[0]
    data.loc[i] = newvec[1]
ED = []
samplesdf = pd.DataFrame(list(zip(ds[:,0],ds[:,1])))
for i in range(1000):
    e = distance.euclidean(data.iloc[i], samplesdf.iloc[i])
    ED.append(e)
print('Euclidean distance value is', st.mean(ED))
pidd3 = copy.deepcopy(pidd2)
pidd3arr = pidd3.to_numpy()
pidd3_pca = PCA(n_components=2).fit_transform(pidd3)    #doing the PCA analysis
pidd3_pca = pd.DataFrame(pidd3_pca, columns=['a1', 'a2'])
print("The variance values are-")
print(round(pidd3_pca.var(), 3))
plt.scatter(pidd3_pca['a1'], pidd3_pca['a2'])
plt.xlabel('a1')
plt.ylabel('a2')
plt.title('Scatter plot for reduced dim data')
plt.show()
corr_matrix = pidd3.corr()
eignvalues, eigenvec = np.linalg.eig(corr_matrix)
print("The eigenvalues are", eignvalues)
print("The eigenvectors are", eigenvec)
evalues = list(eignvalues)
evectors = list(eigenvec)
Eval_Evec = [[], []]
for i in range(8):  
    Eval_Evec[0].append(evalues[i])
    Eval_Evec[1].append(evectors[i])
corresvec = []
max_evalue = []
for i in range(len(evalues)):
    if(Eval_Evec[0][i] == max(Eval_Evec[0])):
        corresvec.append(Eval_Evec[1][i])
        max_evalue.append(Eval_Evec[0][i])
        Eval_Evec[0].pop(i)
        Eval_Evec[1].pop(i)
        break
for i in range(len(evalues)):
    if(Eval_Evec[0][i] == max(Eval_Evec[0])):
        corresvec.append(Eval_Evec[1][i])
        max_evalue.append(Eval_Evec[0][i])
        Eval_Evec[0].pop(i)
        Eval_Evec[1].pop(i)
        break
max_evalue = [round(x, 3) for x in max_evalue]
print("The two largest eigen values are", max_evalue)
print("The corresponding eigen vectors are", corresvec)
evalues.sort(reverse=True)
x = [i for i in range(len(evalues))]
plt.bar(x, evalues)
plt.title('Eigen Values sorted in Descending Order')
plt.xlabel('Index')
plt.ylabel('Eigen Value')
plt.show()
errorlist = []
val = [1,2,3,4,5,6,7,8,9]
def error(a, b):
    eucDistList = []
    for i in range(a.shape[0]):
        sum = 0
        for j in range(a.shape[1]):
            sum += (a[i][j]-b[i][j])**2
        sum = sum**0.5
        eucDistList.append(sum)
    return st.mean(eucDistList)
for i in val:
    pca = PCA(n_components=i)
    ithPCA = pca.fit_transform(pidd3)
    ithdata = pca.inverse_transform(ithPCA)
    eucdist = error(ithdata, pidd3arr)
    errorlist.append(eucdist)
    ithdatadf = pd.DataFrame(ithPCA)
    print('The covariance matrix for l={x}'.format(x=i))
    print(ithdatadf.cov())
plt.plot(xvalues, errorlist)
plt.xlabel('No. of components')
plt.ylabel('Reconstruction error')
plt.title('Line plot to demonstrate reconstruction error vs. components')
plt.show()
print('The covariance matrix for original data')
print(pidd3.cov())