from random import random

def dotProduct(x,y):
    if len(x) !=len(y):
        raise ValueError('Arrays must have same size') 
    n=len(x)
    acc=0.0 # local variable
    for i in range(n):       
        acc=acc+x[i]*y[i]
        #acc+=x[i]*y[i]
    return acc



n=1000

a=[0.0]*n
for i in range(n):
    a[i]=random()    

b=[random() for _ in range(n+1)] #List comprehension
#b=[2*i for i in range(n)] #List comprehension

dot=dotProduct(a,b)

print(f'Dot product is: {dot}')

