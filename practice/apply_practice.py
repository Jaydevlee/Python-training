import pandas as pd

filename = './data/memberInfo_exam.csv'
df = pd.read_csv(filename, index_col='이름')
print(df)

def sungjuk(x):
    if x >= 60 and x < 70:
        return "양"
    elif x >= 70:
        return "미"
sq = df['중간'].apply(sungjuk)
print(sq)