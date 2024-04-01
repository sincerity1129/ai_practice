import pandas as pd
import os


df = pd.read_csv('nlp_basic/basic_liv/pandas/example.csv')
print(df)

print(df.index)

dfs = pd.read_html('https://www.infostock.co.kr/Theme/ThemeDB')
df = dfs[0]  # 첫 번째 테이블을 선택
print(df)