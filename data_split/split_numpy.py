import numpy as np

np_array = np.arange(0,16).reshape((4,4))
print('전체 데이터 :')
print(np_array)

'''
[행,열]
행의 인덱스 설정
열의 인덱스 설정
'''
X = np_array[:, :3]
y = np_array[:,3]

print('X 데이터 :')
print(X)
print('y 데이터 :',y)