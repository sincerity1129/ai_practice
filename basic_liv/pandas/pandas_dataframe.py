import pandas as pd

data = [
    ['1000', 'Steve', 90.72], 
    ['1001', 'James', 78.09], 
    ['1002', 'Doyeon', 98.43], 
    ['1003', 'Jane', 64.19], 
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]

df = pd.DataFrame(data)
print(df)
print("\t")
print("\t")
print("\t")

# columns 지정
df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
print(df)
print("\t")
print("\t")
print("\t")

# 딕셔너리로 생성하기(key -> column, value -> raw)
data = {
    '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
    '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
    '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
    }

df = pd.DataFrame(data)
print(df)
print("\t")
print("\t")
print("\t")

##################################데이터 프레임 컨트롤 해보기######################################
# 앞 부분을 3개만 보기
print(df.head(3))
# 뒷 부분을 3개만 보기
print(df.tail(3))