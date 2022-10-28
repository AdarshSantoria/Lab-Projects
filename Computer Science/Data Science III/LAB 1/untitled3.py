import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
x=pd.read_csv("pima-indians-diabetes.csv")
y=list(x.head())
for i in y:
    print(f'mean of {i} = {np.mean([x[i]])}')
    print(f'median of {i} = {np.median([x[i]])}')
    print(f'mode of {i} = {statistics.mode(x[i])}')
    print(f'min of {i} = {np.min([x[i]])}')
    print(f'max of {i} = {np.max([x[i]])}')
    print(f'standard deviation of {i} = {np.std([x[i]])}')
    if(i=='Age'):
        break
for i in y:
    plt.scatter(x['Age'],x[i])
    plt.xlabel('Age')
    plt.ylabel(i)
    plt.show()
    if(i=='pedi'):
        break
for i in y:
    if(i!='BMI' and i!='class'):
        plt.scatter(x['BMI'],x[i])
        plt.xlabel('BMI')
        plt.ylabel(i)
        plt.show()
for i in y:
    if(i!='Age'):
        print(f'corrcoef of Age with {i} = ',end='')
        print(np.corrcoef(x['Age'],x[i])[0][1])
    if(i!='BMI'):
        print(f'corrcoef of BMI with {i} = ',end='')
        print(np.corrcoef(x['BMI'],x[i])[0][1])
    if(i=='Age'):
        break
plt.hist(x['pregs'])
plt.title('pregs')
plt.show()
plt.hist(x['skin'])
plt.title('skin')
plt.show()
z1=x[x['class']==1]
z0=x[x['class']==0]
plt.hist(z1.groupby('pregs').groups)
plt.title('class = 1')
plt.xlabel('pregs')
plt.show()
plt.hist(z0.groupby('pregs').groups)
plt.title('class = 0')
plt.xlabel('pregs')
plt.show()
for i in y:
    plt.boxplot(x[i])
    plt.title(i)
    plt.show()
    if(i=='Age'):
        break