import pandas as pd                                #importing modules
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
'''1'''
df = pd.read_csv('SteelPlateFaults-2class.csv')
df = df.drop(columns = ['X_Minimum','Y_Minimum','TypeOfSteel_A300','TypeOfSteel_A400']) #dropping unecessary columns
df_group = df.groupby('Class')
df_0 = df_group.get_group(0)
df_1 = df_group.get_group(1)
X_0 = df_0.drop(columns = 'Class')
X_1 = df_1.drop(columns = 'Class')                             #remove class column
Y_0 = df_0['Class']
Y_1 = df_1['Class'] 
x_train, x_test, y_train, y_test=train_test_split(df.iloc[:,0:23], df.iloc[:,23], test_size=0.3, random_state=42,shuffle=True)  #spliting data
x0_train, x0_test, y0_train, y0_test = train_test_split(X_0, Y_0, test_size=0.3, random_state=42, shuffle=True)  #spliting data
x1_train, x1_test, y1_train, y1_test = train_test_split(X_1, Y_1, test_size=0.3, random_state=42, shuffle=True)  #spliting data
best1=0
for i in [2,4,8,16]:                                 #K-N Classification  
    gmm0 = GaussianMixture(n_components=i, covariance_type='full',reg_covar = 1e-4) #G-MM classifier
    gmm0.fit(x0_train)
    gmm1 = GaussianMixture(n_components=i, covariance_type='full',reg_covar = 1e-4)
    gmm1.fit(x1_train)
    s0=gmm0.score_samples(x_test)
    s1=gmm1.score_samples(x_test)
    ans=[]
    for i in range(len(s0)):
        if s0[i]>=s1[i]:
            ans.append(0)
        else:
            ans.append(1)
    cm = confusion_matrix(y_test, ans)         #Testing model
    acc_score = accuracy_score(y_test, ans)    #Spreading data(preprocessing)
    if(i==2 or acc_score>best1):
        best1=acc_score
        qc=i
    print(f'Confusion Matrix for Q = {i} is: \n{cm}')
    print(f'Accuracy Score for  Q= {i} is: {acc_score}')
print(f'Highest accuracy is {best1} for Q = {qc}')
'''2'''
'''a'''
df = pd.read_csv('abalone.csv')
col=list(df.columns)
col.pop()
x_train, x_test = train_test_split(df, test_size=0.3, random_state=42,shuffle=True)  #spliting data
df_train= pd.DataFrame(x_train).to_csv('abalone-train.csv')
corr=list(x_train.corr()['Rings'])
corr.pop()
par=col[corr.index(max(corr))]
print(f'{par} has the highest Pearson correlation coefficient with the target attribute Rings')
model = LinearRegression().fit(np.array(x_train[par]).reshape(-1,1),np.array(x_train['Rings']).reshape(-1,1))
plt.title("Best Fit Train Data") #plotting the graph
plt.xlabel("Predicted Rings")
plt.ylabel("Actual Rings")
plt.scatter(model.predict(np.array(x_train[par]).reshape(-1,1)),np.array(x_train['Rings']).reshape(-1,1))
pred=model.predict(np.array(x_train[par]).reshape(-1,1)).reshape(-1)
a,b=np.polyfit(pred,np.array(x_train['Rings']),1)
plt.plot(pred, a*pred+b,color='red')  
plt.show()
train_error=np.sqrt(mean_squared_error(np.array(x_train['Rings']).reshape(-1,1),model.predict(np.array(x_train[par]).reshape(-1,1))))
print(f'The prediction accuracy on the training data using root mean squared error is {train_error}')
test_error=np.sqrt(mean_squared_error(np.array(x_test['Rings']).reshape(-1,1),model.predict(np.array(x_test[par]).reshape(-1,1))))
print(f'The prediction accuracy on the testing data using root mean squared error is {test_error}')
plt.title("Best Fit Test Data") #plotting the graph
plt.xlabel("Predicted Rings")
plt.ylabel("Actual Rings")
plt.scatter(model.predict(np.array(x_test[par]).reshape(-1,1)),np.array(x_test['Rings']).reshape(-1,1))
plt.show()
'''b'''
model = LinearRegression().fit(np.array(x_train.iloc[:,:-1]),np.array(x_train.iloc[:,-1]))
train_error=np.sqrt(mean_squared_error(np.array(x_train['Rings']).reshape(-1,1),model.predict(x_train.iloc[:,:-1])))
print(f'The prediction accuracy on the training data using root mean squared error is {train_error}')
test_error=np.sqrt(mean_squared_error(np.array(x_test['Rings']).reshape(-1,1),model.predict(x_test.iloc[:,:-1])))
print(f'The prediction accuracy on the training data using root mean squared error is {test_error}')
plt.title("Best Fit Test Data")       #plotting the graph
plt.ylabel("Predicted Rings")
plt.xlabel("Actual Rings")
plt.scatter(np.array(x_test['Rings']).reshape(-1,1),model.predict(x_test.iloc[:,:-1]))
plt.show()
'''c'''
p = [2,3,4,5]
def poly_pred(data):               #Function for prediction of data
    l = []
    for i in p:
        polynomial_features = PolynomialFeatures(degree = i)
        x_poly = polynomial_features.fit_transform(np.array(data[par]).reshape(-1,1))
        regressor = LinearRegression()
        regressor.fit(x_poly, np.array(data['Rings']).reshape(-1,1))
        y_pred = regressor.predict(x_poly)
        error = np.sqrt(mean_squared_error(data['Rings'], y_pred))
        l.append(error)
    return [l,y_pred]             #Prediction accuracy on the training and test data for the different values of degree of the polynomial (p = 2, 3, 4, 5) using root mean squared error (RMSE)
for i in range(len(p)):
    print(f"RMSE Error for train p ={p[i]} is {poly_pred(x_train)[0][i]}")
    print(f"RMSE Error for test p ={p[i]} is {poly_pred(x_test)[0][i]}")
##function for plotting RMSE vs degree of polynomial
def plot2(data,x,y): 
    plt.title(f'Bar graph of RMSE vs degree of polynomial for {data}')
    plt.xlabel('Degree of polynomial')
    plt.ylabel('RMSE')
    plt.bar(x, y)
    plt.show()
plot2('Traning Data',p,poly_pred(x_train)[0]) #Plotting the RMSE vs degree of polynomial graph
plot2('Test Data',p,poly_pred(x_test)[0])
plt.title('Best Fit Polynomial')         #plotting scatter plot for best fit polynomial
plt.xlabel(par)
plt.ylabel("Predicted Rings")
plt.scatter(x_train[par],poly_pred(x_train)[1])
plt.show()
plt.title('Predicted vs Real')           #the scatter plot of the actual number of Rings (x-axis) vs the predicted number of Rings (y-axis) on the test data for the best degree of the polynomial (p)
plt.scatter(x_test['Rings'],poly_pred(x_test)[1])
plt.show()
#Multivariate nonlinear regression model using polynomial regression to predict Rings
'''d'''
def multi_poly_pred(data):               #Function for prediction of data
    l = []
    for i in p:
        polynomial_features = PolynomialFeatures(degree = i)
        x_poly = polynomial_features.fit_transform(np.array(data.iloc[:,:-1]))
        regressor = LinearRegression()
        regressor.fit(x_poly, np.array(data['Rings']))
        y_pred = regressor.predict(x_poly)
        error = np.sqrt(mean_squared_error(data['Rings'], y_pred))
        l.append(error)
    return [l,y_pred]
for i in range(len(p)):
    print(f"RMSE Error for train p ={p[i]} is {multi_poly_pred(x_train)[0][i]}")
    print(f"RMSE Error for test p ={p[i]} is {multi_poly_pred(x_test)[0][i]}")
plot2('Traning Data',p,multi_poly_pred(x_train)[0])  #Plotting the RMSE vs degree of polynomial graph
plot2('Test Data',p,multi_poly_pred(x_test)[0])
plt.title('Predicted vs Real')            #Plotting the best fit curve using the best fit model on the training data
plt.scatter(x_test['Rings'],multi_poly_pred(x_test)[1])
plt.show()