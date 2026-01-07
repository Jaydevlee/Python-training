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
# print(myframe)

#DataFrame에서 데이터 추출
#iloc 함수 활용하여 1행만 추출하기
# print(myframe.iloc[1])  
# print(myframe.iloc[[1]])
# print(myframe.iloc[[1, 3]])
# print(myframe.iloc[0::2])

# loc을 사용하여 행이름으로 데이터 추출
# print(myframe.loc[['이순신']])
# print(myframe.loc[['이순신', '강감찬']])

# #choice()함수로 랜덤 복원 추출
# mytarget = np.random.choice(myframe.index, 3) # index 3개 랜덤 추출
# print(myframe.loc[mytarget])

#loc으로 행과 열의 데이터 추출
# print(myframe.loc[['강감찬'], ['광주']])
# print(myframe.loc[['연산군', '강감찬'], ['광주', '목포']])

# 연속적인 데이터 추출
# print(myframe.loc['김유신' : '광해군', '광주' : '목포'])

# boolean 타입으로 데이터 추출
# print(myframe.loc[[False, True, True, False, True]]) # 이순신 광해군 제외

#관계 연산자 활용
print(myframe.loc[myframe['부산'] <= 100])
print(myframe.loc[myframe['목포'] == 140])
