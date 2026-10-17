#adding two arrays using numpy
import numpy as np
"""
array =[1,3,2,4,5]
np.array(array)
array=array*2
print(array)
brray = [1,2,3,4,5,5,6,7,8,9]
brray = np.array(brray)
print(array+brray)
print(type(array))
array2 = np.array([100,300,500,700,900],dtype=np.int16)
print(array2.dtype)
print(f"{array2.nbytes} bytes")
array3 = np.array([1.1,1.2,1.3,1.4,1.5],dtype=np.float16)
print(array3.dtype)
if array3.dtype=="float16":
    print(True)
else:
    print(False)
array4 = np.array(["hi", "bye", "hii"], dtype=np.str_)
print(array4, "\n", array4.dtype, "\n", array4.nbytes, "\n")
array5 = np.array([1,2,3,4,5,"hiiiiii"],dtype="object")
print(array5 , sep="/n")
print(array5.dtype)
"""
#2d,3d array

array6=np.array([1,3,4,5])
print(array6.ndim)
matrix =np.array([
    [
        [1,3,5,7],
        [2,4,6,8]
    ],
    [
        [12,32,52,72],
        [22,42,62,82]

    ],
])
print(matrix.ndim,matrix[1][1][2])#single dim indexing
print(matrix.ndim,matrix[1,1,2])#multi dimensional indexing
print(matrix.ndim,matrix.shape)#.shape to find shape
array7 = np.array( [
        [1,3,5,7,4],
        [2,4,6,8,5]
    ])
print(array7.ndim, sep="/n")
print(array7.reshape(5,2))