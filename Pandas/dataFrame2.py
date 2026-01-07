import pandas as pd #데이터 분석용 라이브러리
import numpy as np # 데이터 계산용 라이브러리

myindex = ['이순신', '김유신', '강감찬', '광해군', '연산군'] # 행으로 사용할 이름 목록
mycolumns = ['서울', '부산', '광주', '목포', '경주'] # 열 이름으로 사용할 지역 목록
# 1부터 25까지 10을 곱한 값을 리스트로 저장
mylist = list(10 * onedata for onedata in range(1, 26)) 
# print(mylist)

#DataFrame 생성
myframe = pd.DataFrame(np.reshape(mylist, (5, 5)),
                      index = myindex,
                      columns = mycolumns)

# all(), any() 함수
cond1 = myframe['부산'] >= 70 #부산의 값이 70이상인 행인 경우 true
cond2 = myframe['목포'] >= 140 # 목포의 값이 70이상인 행인 경우 true
print(cond1)
print(cond2)
df = pd.DataFrame([cond1, cond2])
print(df)
print(myframe.loc[df.all()])
print(myframe.loc[df.any()])