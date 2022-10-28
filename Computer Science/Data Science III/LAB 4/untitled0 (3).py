'''
Author : Adarsh Santoria
Roll : B21176
Ph : 8597849862
'''
import pandas as pd                                #importing modules
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
'''1'''
df = pd.read_csv('SteelPlateFaults-2class.csv')
X = df.iloc[:,0:27]                                #remove class column
Y = df.iloc[:, 27]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42,shuffle=True)  #spliting data
df_train= pd.DataFrame(x_train)
df_test = pd.DataFrame(x_test)
df_train.to_csv('SteelPlateFaults-train.csv')
df_test.to_csv('SteelPlateFaults-test.csv')
best=0
for i in [1,3,5]:                                 #K-N Classification  
    K_classifier = KNeighborsClassifier(n_neighbors=i, p=2, metric='euclidean') #K-N classifier
    K_classifier.fit(x_train, y_train)
    y_pred = K_classifier.predict(x_test)
    cm = confusion_matrix(y_test, y_pred)         #Testing model
    acc_score = accuracy_score(y_test, y_pred)    #Spreading data(preprocessing)
    if(i==1 or acc_score>best):
        best=acc_score
        neigh=i
    print(f'Confusion Matrix for K = {i} is: \n{cm}')
    print(f'Accuracy Score for K = {i} is: {acc_score}')
print(f'Highest accuracy is {best} for K = {neigh}')
'''2'''
Scale = MinMaxScaler()                             #min-max normalization of data
df_minmax_train = pd.DataFrame(Scale.fit_transform(df_train), columns=df_train.columns)  #Puting normalised data into its own csv files
df_minmax_train.to_csv('SteelPlateFaults-train-Normalised.csv')
df_minmax_test = pd.DataFrame(Scale.fit_transform(df_test), columns=df_test.columns)
df_minmax_test.to_csv('SteelPlateFaults-test-normalised.csv')
best1=0
for i in [1,3,5]:                                       #repeating same step as in previous one
    K1_classifier = KNeighborsClassifier(n_neighbors=i, p=2, metric='euclidean')
    K1_classifier.fit(df_minmax_train, y_train)
    y_pred = K1_classifier.predict(df_minmax_test)
    cm = confusion_matrix(y_test, y_pred)
    acc_score = accuracy_score(y_test, y_pred)
    if(i==1 or acc_score>best1):
        best1=acc_score
        neigh=i
    print(f'Confusion Matrix for K = {i} is: \n{cm}')
    print(f'Accuracy Score for K = {i} is: {acc_score}')
print(f'Highest accuracy is {best1} for K = {neigh}')
'''3'''
x_train, x_test = train_test_split(df, test_size=0.3, random_state=42,shuffle=True)   #splitting data
x_test = x_test.drop(columns = ['Class','TypeOfSteel_A300','TypeOfSteel_A400', 'Steel_Plate_Thickness']) #dropping unecessary columns
x_train_0 = x_train.groupby('Class').get_group(0)
x_train_1 = x_train.groupby('Class').get_group(1)
mean_0 = x_train_0.drop(columns = ['Class','TypeOfSteel_A300','TypeOfSteel_A400', 'Steel_Plate_Thickness']).mean()
cov_0 = np.cov(x_train_0.drop(columns = ['Class','TypeOfSteel_A300','TypeOfSteel_A400', 'Steel_Plate_Thickness']).T)
det_0 = np.linalg.det(cov_0)              #finding covariance and its inverse
cov_0_inv = np.linalg.inv(cov_0)
mean_1 = x_train_1.drop(columns = ['Class','TypeOfSteel_A300','TypeOfSteel_A400', 'Steel_Plate_Thickness']).mean()
cov_1 = np.cov(x_train_1.drop(columns = ['Class','TypeOfSteel_A300','TypeOfSteel_A400', 'Steel_Plate_Thickness']).T)
det_1 = np.linalg.det(cov_1)              #finding covariance and its inverse
cov_1_inv = np.linalg.inv(cov_1)
arr = []
for j in x_test.itertuples():
    i = np.array(j)
    i = np.delete(i,0)
    likely_0 = (1/((2*(np.pi))**(len(i)/2)))*((1/det_0)**0.5)*np.exp((-1*1/2)*np.dot(np.dot(((i-mean_0).T),cov_0_inv),(i-mean_0)))
    likely_1 = (1/((2*(np.pi))**(len(i)/2)))*((1/det_1)**0.5)*np.exp((-1*1/2)*np.dot(np.dot(((i-mean_1).T),cov_1_inv),(i-mean_1)))
    if likely_0>=likely_1:
        arr.append(0)
    elif likely_0<likely_1:
        arr.append(1)
print(confusion_matrix(arr,y_test))
print(accuracy_score(arr,y_test))
print("Best values are:",best, best1,accuracy_score(arr,y_test))