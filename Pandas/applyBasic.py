import pandas as pd

filename = './data/memberInfo.csv'
df = pd.read_csv(filename, index_col='id')

print('시리즈와 apply 메서드')
print(df)
print('-' * 20)

# 국어 점수에 5를 더하는 메소드
def plus5(x):
    return x + 5
print("apply 함수를 적용한 결과")
sq = df['kor'].apply(plus5)
print(sq)

# n배를 곱해주는 함수
def mult(x, n):
    return n * x
ex = df['kor'].apply(mult, n=2)
print(ex)
print('-' * 30)

# 열 방향으로 평균 값을 구하는 함수

# 행 방향으로 평균 값을 구하는 함수