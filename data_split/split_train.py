from sklearn.model_selection import train_test_split
import numpy as np

np_array = np.arange(0,16).reshape((4,4))
print('1. 전체 데이터 :')
print(np_array)
print("\t")
print("\t")

'''
[행,열]
행의 인덱스 설정
열의 인덱스 설정
'''
X = np_array[:, :3]
y = np_array[:,3]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=1234)
print('2. X 전체 데이터 :')
print(X)
print('y 전체 데이터 :')
print(y)
print("\t")
print("\t")


# 임의로 X와 y 데이터를 생성
X, y = np.arange(10).reshape((5, 2)), range(5)

print('3. X 전체 데이터 :')
print(X)
print('y 전체 데이터 :')
print(list(y))
print("\t")
print("\t")

# 7:3의 비율로 훈련 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

print('4. X 훈련 데이터 :')
print(X_train)
print('X 테스트 데이터 :')
print(X_test)
print("\t")
print("\t")

print('y 훈련 데이터 :')
print(y_train)
print('y 테스트 데이터 :')
print(y_test)
print("\t")
print("\t")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print('5. y 훈련 데이터 :')
print(y_train)
print('y 테스트 데이터 :')
print(y_test)
print("\t")
print("\t")

# random_state을 이전의 값이었던 1234로 변경
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

print('6. y 훈련 데이터 :')
print(y_train)
print('y 테스트 데이터 :')
print(y_test)
print("\t")
print("\t")

# 수동으로 데이터 분리 방법
# 실습을 위해 임의로 X와 y가 이미 분리 된 데이터를 생성
X, y = np.arange(0,24).reshape((12,2)), range(12)

print('7. X 전체 데이터 :')
print(X)
print('y 전체 데이터 :')
print(list(y))
print("\t")
print("\t")

num_of_train = int(len(X) * 0.8) # 데이터의 전체 길이의 80%에 해당하는 길이값을 구한다.
num_of_test = int(len(X) - num_of_train) # 전체 길이에서 80%에 해당하는 길이를 뺀다.
print('8. 훈련 데이터의 크기 :',num_of_train)
print('테스트 데이터의 크기 :',num_of_test)
print("\t")
print("\t")

X_test = X[num_of_train:] # 전체 데이터 중에서 20%만큼 뒤의 데이터 저장
y_test = y[num_of_train:] # 전체 데이터 중에서 20%만큼 뒤의 데이터 저장
X_train = X[:num_of_train] # 전체 데이터 중에서 80%만큼 앞의 데이터 저장
y_train = y[:num_of_train] # 전체 데이터 중에서 80%만큼 앞의 데이터 저장

print('9. X 테스트 데이터 :')
print(X_test)
print('y 테스트 데이터 :')
print(list(y_test))
print("\t")
print("\t")