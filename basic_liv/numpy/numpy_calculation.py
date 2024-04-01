import numpy as np

x = np.array([1,2,3])
y = np.array([4,5,6])

# result = np.add(x, y)와 동일.
result = x + y
print(result)

# result = np.subtract(x, y)와 동일.
result = x - y
print(result)

# result = np.multiply(result, x)와 동일.
result = result * x
print(result)

''''
mat1
1,2 
3,4

mat2
5,6
7,8

19(1*5+2*7) 22(1*6+2*8)
43(3*5+4*7) 50(3*6+4*8) 
'''
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
mat3 = np.dot(mat1, mat2)
print(mat3)