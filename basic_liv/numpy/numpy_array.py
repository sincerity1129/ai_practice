import numpy as np

# 1차원 배열
vec = np.array([1, 2, 3, 4, 5])
print(vec)

# 2차원 배열
mat = np.array([[10, 20, 30], [ 60, 70, 80]]) 
print(mat)

print('vec의 타입 :',type(vec))
print('mat의 타입 :',type(mat))

'''
ndim: dimension
shape: array 크기
'''
print('vec의 축의 개수 :',vec.ndim)
print('vec의 크기(shape) :',vec.shape)

print('mat의 축의 개수 :',mat.ndim)
print('mat의 크기(shape) :',mat.shape)