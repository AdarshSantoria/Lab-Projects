import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf
from sklearn.model_selection import train_test_split
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
'''1'''
x=pd.read_csv("daily_covid_cases.csv")
plt.rcParams['figure.figsize'] = (16, 9)
plt.plot(pd.to_datetime(x['Date']),x['new_cases'])
plt.show()
x=x.iloc[:,1]
dataframe = pd.concat([x.shift(1), x], axis=1)
print(dataframe.corr())
plt.xlabel('Generated one-day lag time sequence')
plt.ylabel('Given time sequence')
plt.scatter(dataframe.iloc[:,1],dataframe.iloc[:,0])
plt.show()
dataframe = pd.concat([x.shift(6),x.shift(5),x.shift(4),x.shift(3),x.shift(2),x.shift(1), x], axis=1)
dataframe.columns = ['t+6', 't+5', 't+4', 't+3','t+2','t+1','t']
print(dataframe.corr()['t'])
plt.ylabel('Corelation Coeficient')
plt.plot(['t+6', 't+5', 't+4', 't+3','t+2','t+1','t'][::-1],dataframe.corr()['t'][::-1])
plot_acf(x)
plt.show()
'''2'''
x=pd.read_csv("daily_covid_cases.csv")
x_train,x_test=train_test_split(x,test_size=0.35,shuffle=False)
x1_train,x1_test=train_test_split(x,test_size=0.35,shuffle=False)
plt.title('x_train')
plt.plot(pd.to_datetime(x_train['Date']),x_train['new_cases'])
plt.show()
plt.title('x_test')
plt.plot(pd.to_datetime(x_test['Date']),x_test['new_cases'])
plt.show()
ar_model = AutoReg(x_train['new_cases'], lags=5).fit()
coef = ar_model.params
for i in range(len(coef)):
    print(f'w{i} is {coef[i]}')
window = 1
x_train=list(x_train['new_cases'])
x_test=list(x_test['new_cases'])
history = x_train[len(x_train)-window:]
predictions = [] # List to hold the predictions, 1 step at a time
for t in range(len(x_test)):
    length = len(history)
    lag=[]
    for i in range(length-window,length):
        lag.append(history[i])
    yhat = coef[0]
    for d in range(window):
        yhat += coef[d+1] * lag[window-d-1] # Add other values
    obs = x_test[t]
    predictions.append(yhat) #Append predictions to compute RMSE later
    history.append(obs)
plt.title('Actual Vs Predicted Values')
plt.scatter(x1_test['new_cases'],predictions)
plt.show()
plt.title('Predicted Values')
plt.plot(pd.to_datetime(x1_test['Date']),predictions)
plt.show()
plt.title('Actual Values')
plt.plot(pd.to_datetime(x1_test['Date']),x1_test['new_cases'])
plt.show()
rmse = (mean_squared_error(x_test, predictions))**0.5
print('RMSE for test data : ', rmse)
print('MAPE for test data : ', np.mean(np.abs((np.array(x_test) - np.array(predictions)) / np.array(x_test))) * 100)
'''3'''
k = [1, 5, 10, 15, 25]
R = []
M = []
for j in k:
    window = j
    model = AutoReg(x_train, lags=j)
    model_fit = model.fit()
    coef = model_fit.params
    history = list(x_train[len(x_train)-window:])
    predictions = list()
    for t in range(len(x_train), len(x)):
        length = len(history)
        lag=[]
        for i in range(length-window,length):
            lag.append(history[i])
        yhat = coef[0]
        for d in range(window):
            yhat += coef[d+1] * lag[window-d-1]
        obs = x_test[t-len(x_train)]
        predictions.append(yhat)
        history.append(obs)
    rmse = (mean_squared_error(x_test, predictions))**0.5
    R.append(rmse)
    print(f'RMSE for test data for lag {j}', "is :", rmse)
    MAPE = np.mean(np.abs((np.array(x_test) - np.array(predictions)) / np.array(x_test))) * 100
    M.append(MAPE)
    print(f'MAPE for test data for lag {j}', "is :", MAPE)
plt.bar(k, R)
plt.title("Barchart of RMSE")
plt.show()
plt.bar(k, M)
plt.title("Barchart of  MAPE")
plt.show()
'''4'''
data = pd.read_csv('daily_covid_cases.csv')
z = 2/np.sqrt(len(x))
test = data.iloc[len(x_train):, 1]
acf = sm.tsa.acf(data["new_cases"], nlags=len(x), fft=True)
window = 0
for i in acf:
    if i > z:
        window += 1
    else :
        break
print("optimal no of lags :", window)
model = AutoReg(x_train, lags=window)
model_fit = model.fit()
coef = model_fit.params
history = list(x_train[len(x_train)-window:])
predictions = []
for t in range(len(x_test)):
    length = len(history)
    lag=[]
    for i in range(length-window,length):
        lag.append(history[i])
    print(lag)
    print(history)
    yhat = coef[0]
    for d in range(window):
        yhat += coef[d+1] * lag[window-d-1]
    obs = x_test[t]
    predictions.append(yhat)
    history.append(obs)
rmse = (mean_squared_error(x_test, predictions))**0.5
print('RMSE for test data : ', rmse)
print('MAPE for test data : ', np.mean(np.abs((np.array(x_test) - np.array(predictions)) / np.array(x_test))) * 100)