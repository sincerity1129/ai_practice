import pandas as pd

# 데이터 생성
data = {
    '날짜': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    '지표': ['A', 'B', 'A', 'B'],
    '값': [10, 20, 15, 25]
}

df = pd.DataFrame(data)
print("1. ",df)
print("\t")

# 피벗팅
pivoted_df = df.pivot(index='날짜', columns='지표', values='값')
print(pivoted_df)
print("\t")
print("\t")


# 데이터 생성
data = {
    'A': [1, 3],
    'B': [2, 4]
}

df = pd.DataFrame(data)
print("2. ",df)
print("\t")

# 스택
stacked_df = df.stack()
print(stacked_df)
print("\t")

#언스택
unstacked_df = stacked_df.unstack()
print(unstacked_df)
print("\t")
print("\t")

# 데이터 생성
data = {
    '이름': ['John', 'Alice'],
    '수학': [90, 95],
    '영어': [85, 92]
}

df = pd.DataFrame(data)
print("3. ",df)
print("\t")

# 멜팅
melted_df = pd.melt(df, id_vars=['이름'], value_vars=['수학', '영어'], var_name='과목', value_name='성적')
print(melted_df)
print("\t")
print("\t")

# 데이터 생성
data = {
    '이름': ['John', 'Alice', 'John', 'Alice'],
    '과목': ['수학', '수학', '영어', '영어'],
    '성적': [90, 95, 85, 92]
}

df = pd.DataFrame(data)
print("4. ",df)
print("\t")


# 그룹화 및 집계
grouped_df = df.groupby('이름')["성적"].agg(['mean', 'min', 'max', 'count'])
print(grouped_df)