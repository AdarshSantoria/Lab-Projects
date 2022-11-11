import pandas as pd                                #importing modules
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.optimize import linear_sum_assignment
from sklearn.mixture import GaussianMixture
from sklearn.cluster import DBSCAN
from scipy import spatial as spatial
'''1'''
df = pd.read_csv('Iris.csv')
x_train=df.iloc[:,:4]
y_train=df.iloc[:,4]
x_train1 = pd.DataFrame(PCA(n_components = 2).fit_transform(x_train))
eigenvalues, eigenvec = np.linalg.eig(x_train.corr())
eigenvec=eigenvec.T
x = [i for i in range(len(eigenvalues))]
plt.bar(x, eigenvalues)
plt.title('Eigen Values')
plt.xlabel('Index')
plt.ylabel('Eigen Value')
plt.show()
l=eigenvalues[:2]
l1=eigenvec[:2]
for i in range(2,4):
    if(l[0]<l[1]):
        l[0],l[1]=l[1],l[0]
        l1[0],l1[1]=l1[1],l1[0]
    if(eigenvalues[i]>l[1]):
        eigenvalues[i],l[1]=l[1],eigenvalues[i]
        eigenvec[i],l1[1]=l1[1],eigenvec[i]
print("Leading eigenvalues are", l)
print("Leading eigenvectors are", l1)
plt.title('Leading Eigen Vectors Directions')
plt.quiver(0,0, eigenvec[0][0], eigenvec[0][1], label='v1')
plt.quiver(0,0, eigenvec[1][0], eigenvec[1][1], label='v2')
plt.show()
'''2'''
km=KMeans(n_clusters=3)
y_pred=km.fit_predict(x_train1)
def plot(a):
    x_train1['cluster']=y_pred
    y1=x_train1[x_train1.cluster==0]
    y2=x_train1[x_train1.cluster==1]
    y3=x_train1[x_train1.cluster==2]
    plt.scatter(y1[0],y1[1],label='1')
    plt.scatter(y2[0],y2[1],label='2')
    plt.scatter(y3[0],y3[1],label='3')
    if(a=='km'):
        plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],label='center')
    else:
        plt.scatter(gmm.means_[:,0], gmm.means_[:,1],label='cluster centres')
    plt.legend()
    plt.show()
plot('km')
print(f'Distortion measure is {km.inertia_}')
def purity_score(y_true, y_pred):
    # compute contingency matrix (also called confusion matrix)
    contingency_matrix=metrics.cluster.contingency_matrix(y_true, y_pred)
    # Find optimal one-to-one mapping between cluster labels and true labels
    row_ind, col_ind = linear_sum_assignment(-contingency_matrix)
    # Return cluster accuracy
    return contingency_matrix[row_ind,col_ind].sum()/np.sum(contingency_matrix)
print(f'Purity Score is {purity_score(y_train,y_pred)}')
'''3'''
K=[2,3,4,5,6,7]
D=[]
for i in K:
    km=KMeans(n_clusters=i)
    y_pred=km.fit_predict(x_train1)
    print(f'Distortion measure for {i} clusters is {km.inertia_}')
    D.append(km.inertia_)
    print(f'Purity Score is for {i} clusters {purity_score(y_train,y_pred)}')
plt.title('K vs distortion measure')
plt.plot(K,D)
plt.show()
print('From the above graph we can see the optimum value of K is 3')
'''4'''
gmm = GaussianMixture(n_components = 3).fit(x_train1)
y_pred = gmm.predict(x_train1)
plot('gmm')
print(f'Distortion measure is {sum(gmm.score_samples(x_train1))}')
print(f'Purity Score is {purity_score(y_train,y_pred)}')
'''5'''
D=[]
for i in K:
    gmm = GaussianMixture(n_components = i).fit(x_train1)
    y_pred=gmm.predict(x_train1)
    print(f'Distortion measure is {sum(gmm.score_samples(x_train1))}')
    D.append(sum(gmm.score_samples(x_train1)))
    print(f'Purity Score is for {i} clusters {purity_score(y_train,y_pred)}')
plt.title('K vs distortion measure')
plt.plot(K,D)
plt.show()
print('From the above graph we can see the optimum value of K is 3')
'''6'''
def dbscan_predict(dbscan_model, X_new, metric=spatial.distance.euclidean):
# Result is noise by default
    y_new = np.ones(shape=len(X_new), dtype=int)*-1
# Iterate all input samples for a label
    for j, x_new in enumerate(X_new):
# Find a core sample closer than EPS
        for i, x_core in enumerate(dbscan_model.components_):
            if metric(x_new, x_core) < dbscan_model.eps:
# Assign label of x_core to x_new
                y_new[j] = dbscan_model.labels_[dbscan_model.core_sample_indices_[i]]
                break
    return y_new
x_train1=x_train1.drop(columns=['cluster'])
x_train1 = np.asmatrix(x_train1)
e=[1,5]
mn=[4,10]
for i in e:
    for j in mn:
        dbscan_model=DBSCAN(eps=i, min_samples=j).fit(x_train1)
        y_pred=dbscan_predict(dbscan_model, x_train1, metric=spatial.distance.euclidean)
        plt.scatter(np.array(x_train1[:,0]),np.array(x_train1[:,1]),c=y_pred)
        plt.show()
        print(f'Purity Score is for {i} clusters {purity_score(y_train,y_pred)}')
        #dbtest = dbscan_predict(x_train, x_train1, metric =spatial.distance.euclidean)
