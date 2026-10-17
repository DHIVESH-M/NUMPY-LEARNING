import numpy as np
# arr=np.array([[1,2,3,4,5],
#               [6,7,8,9,10]])
# brr=np.array([[1,2,3,4,5],
#               [6,7,8,9,10]])
# a=np.sum(arr,axis=1)#row wise sum
# b=np.sum(brr,axis=0)#column wise sum
# print(a)
# print(b)
arr=np.array([
    [1,20,3],
    [40,5,60]
    ])
brr=np.array([1,2,3])
print(brr[brr<3])
print(brr<3)
print(brr)
print(arr[arr.sum(axis=1)>50])
crr = np.where(arr%2==0,arr,"faah")
print(crr)