import matplotlib.pyplot as plt                                     #importing modules
import pandas as pd
import numpy as np
x= pd.read_csv("Cowin_Vaccine_Data_Districtwise.csv", header=[0,1]) #reading csv file and grouping dates to months
k= x[x[('State','Unnamed: 2_level_1')]=="Delhi"]                    #making two datset k & k1 to store inputs of Delhi and Mumbai respectively
k1= x[x[('District','Unnamed: 5_level_1')]=='Mumbai']
'''a'''
# obtaining data for first dose from filtered data 
kk= k.xs('First Dose Administered', axis=1, level=1)                #choosing 1st axis for index
kk2= k.xs("Second Dose Administered", axis=1, level=1)
kk1= k1.xs('First Dose Administered', axis=1, level=1)
kk3= k1.xs("Second Dose Administered", axis=1, level=1)
# finding vaccination coverage for delhi and mumbai
delhi_first_dose= kk.sum()/20591874                                 #Finding first dose coverage as per questions
# defining sticks labels
y= pd.date_range(start=pd.to_datetime(delhi_first_dose.index[0], infer_datetime_format=True), end=pd.to_datetime(delhi_first_dose.index[-1], infer_datetime_format=True), freq="M").strftime("%Y/%m")
#Plotting of graph
plt.plot(kk.sum()/20591874, label="Delhi First dose")
plt.plot(kk1.sum()/20667656, label="Delhi Second dose")
plt.plot(kk2.sum()/20591874, label="Mumbai Frist dose")
plt.plot(kk3.sum()/20667656, label="Mumbai Second Dose")
plt.legend()                                                        #showing labels on graph
plt.xticks(ticks=np.linspace(0, len(delhi_first_dose), len(y)), labels=y, rotation=50)
plt.ylabel("Percentage")                                            #titleing and naming the two axises
plt.xlabel("Time ")
plt.title("Vaccination Coverage of Delhi and Mumbai")
plt.show()
# finding correlation in delhi 
'''b'''
#Similarly solving like initials
sessions_data= k.xs('Sessions', level=1, axis=1)/1400
a= k.xs('First Dose Administered', level=1, axis=1).corrwith(sessions_data).mean()
print("Correlation between First Dose Coverege with sessions in Delhi is ",a )
sites_data= k.xs('Sites ', level=1, axis=1)/1400
b= k.xs('First Dose Administered', level=1, axis=1).corrwith(sites_data).mean()
print("Correlation between First Dose coverage and sites in Delhi is : ", b)
# finding correlatin in mumbai 
a1= k1.xs('First Dose Administered', level=1, axis=1).T.corrwith(k1.xs('Sessions', level=1, axis=1).T).mean()
print("Correlation between First Dose Coverege with sessions in Mumbai is ",a1 )
b1= k1.xs('First Dose Administered', level=1, axis=1).T.corrwith(k1.xs('Sites ', level=1, axis=1).T).mean()
print("Correlation between First Dose coverage and sites in Mumbai is : ", b1)
# Finding maximum state with first does coverage
dt= x.xs('First Dose Administered', level=1, axis=1).T.sum()
#running for loop to find index of maxima
r=0
for i in range(len(dt)):
    if dt[i]==max(dt):
        r=i
        break
'''c'''
print("State with highest vaccination Coverege is ", x[('State','Unnamed: 2_level_1')][r])
