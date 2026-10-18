import numpy as np
a = np.array([[1,2],
              [4,5]])
b = np.array([[7,7],
              [8,8]])
print(np.matmul(a,b))
print(np.dot(a,b))
print(b.T)
print(np.linalg.det(a))