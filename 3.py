import numpy as np
a=np.zeros(10)
print(a)
b=np.ones(10)
print(b)
c=np.full(10,5)# to create an array of 10 elements with all values as 5
print(c)
d=np.eye(3) # to create a 3x3 identity matrix
print(d)
e=np.empty(10) # to create an array of 10 elements with random values
print(e)
f=np.arange(0,100,20) # to create an array of values from 0 to 100 with a step of 10
print(f)
g = np.linspace(0,100,10) # to create an array of 5 values between 0 and 100
print(g)
#can also use mean, median, std, var, min, max, argmin, argmax, sum, prod, cumsum, cumprod, sort, argsort, unique etc.
