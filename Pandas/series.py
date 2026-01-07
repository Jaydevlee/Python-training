import pandas as pd

#series 생성
myindex = ['서울', '부산', '광주', '대구', '울산', '목포', '여수']  #배열의 index 역할
mylist = [50, 60, 40, 80, 70, 30, 20]
myseries = pd.Series(data = mylist, index = myindex)
# print(myseries)

# #serise의 값 불러오기
# print(myseries[['대구']]) # index이름으로 불러오기
# print(myseries['대구' : '목포']) # index로 슬라이싱
# print(myseries[['대구', '여수']]) # 분리되어 있는 데이터를 가져오기
# print(myseries[[2]]) # 정수를 사용하여 데이터 읽기

# 슬라이싱 활용
# print(myseries[0:5:2])
# print(myseries[[1, 3, 5]])
# print(myseries[3:6])

# 시리즈 내부 값 변경
myseries[2] = 22 # index 2의 값 변경
myseries[2:5] = 33 # index 2부터 4까지 값 변경
myseries[['서울', '대구']] = 55
myseries[0::2] = 77 #짝수 행만 변경

print(myseries) #변경 내용 확인