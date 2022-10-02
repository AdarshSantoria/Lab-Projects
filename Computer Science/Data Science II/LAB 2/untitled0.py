#P(x) is probability of 'x'
'''Ques 1'''
a=float(input("P(dots sent):"))            #eg:-P(a) is probability of dots sent     
b=float(input("P(dot is mistakely received as dash):"))  
print("P(dot sent/ dot received)=",(a*(1-b))/(a*(1-b)+(1-a)*b))
#probability of dot sent given dot recieved is obtained by taking case when dot was sent
# & recieved out of dot was (sent & recieved) and (sent & but mistakely recieved as dash)
'''Ques 2'''
x,y,z=int(input("defective :")),int(input("partially defective :")),int(input("acceptable :"))
#x,y,z are number of defective, partially sefective & acceptable transistors respectively
#Taking x,y & z  as 2,3,4 as an example
print("p(accepted/ non defective) :", z/(y+z))
#probability of accepted given non defective is obtained by taking acceptable transistors
#out of non defective(partially defective & acceptable)
'''Ques 3'''
file=open("fileA-TimeMachine.txt",'r',encoding='Latin-1')
f=file.read().replace('\n','')                #f is text data of the file
f.lower()                                     #lower casing all text of f
data=''                                       #assuming data a variable
for i in f:                                   #to take only alphabets
    if ord('a')<=ord(i)<=ord('z'):
        data+=i
def P(X,data):                                
#making a function P(X,data) to calculate probability of X in data
    count=data.count(X)                       #count is number of X is in data
    return count/len(data)                       
#probability is obtained as length of data is sample space
def P1(X,Y,data):
#making a function P(X,Y,data) to calculate probability of YX in data 
    count=data.count(Y+X)                     #count is number of YX is in data
    sample=data.count(Y)                      #sample is number of Y is in data
    return count/sample
#probability of X given Y before
X=input("X:")                                 #X is the input of first variable
Y=input("Y:")                                 #Y is the input of first variable
#Taking 1st & 2nd input as 'x' and 'y' respectively as an example
print("P(X) : ",P(X,data))
print("P(Y) : ",P(Y,data))
print("P(X|Y) :",P1(X,Y,data))
print("P(Y|X) :",P1(Y,X,data))                #probabilities are obtained