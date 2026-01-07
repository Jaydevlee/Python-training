import pandas as pd

dict1 = {'name' : ['홍길동', '홍길동', '김철수', '박영희', '김철수', '김철수', '홍길동'],
         'korean': range(7)}
df1 = pd.DataFrame(dict1)
# print(df1)

dict2 = {'name' : ['김철수', '홍길동', '심수봉'],
        'english': range(3)}
df2 = pd.DataFrame(dict2)
# print(df2)

# # print('\n# merge()메소드를 이용하여 데이터 합치기')
# # print(pd.merge(df1, df2, on='name'))

# print("\n# how='outer'를 이용하여 full outer join 하기")
# print(pd.merge(df1, df2, how='outer'))

#print('\n# 양쪽에 동일 이름의 칼럼이 존재하지 않는 경우')
dic3 = {'leftkey':['홍길동', '홍길동', '김철수', '박영희', '김철수', '김철수', '홍길동'],
        'korean' : range(7)}
df3 = pd.DataFrame(dic3)
# print(df3)

dic4 = {'rightkey' : ['김철수', '홍길동', '심수봉'],
        'english': range(3)}
df4 = pd.DataFrame(dic4)
# print(df4)

# print('\n# left_on과 right_on 사용')
# print(pd.merge(df3, df4, left_on='leftkey', right_on='rightkey'))

dict5 = {'key1' : ['김철수', '김철수', '박영희'],
         'key2' : ['one', 'two', 'three'],
         'leftval' : [1, 2, 3]}
left = pd.DataFrame(dict5)
print(left)

dict6 = {'key1' : ['김철수', '김철수', '박영희', '박영희'],
         'key2' : ['one', 'one', 'one', 'two'],
         'leftval' : [4, 5, 6, 7]}
right = pd.DataFrame(dict6)
print(right)

print('\n# 여러 개의 칼럼 병합')
mylist = ['key1', 'key2']
print(pd.merge(left, right, on=mylist, how='outer'))

print('\n# suffixes 옵션 사용')
print(pd.merge(left, right, on='key1', suffixes=('_왼쪽', '_오른쪽')))

# 색인을 이용한 merge
newdf1 = df1.set_index('name')
newdf2 = df2.set_index('name')
print(pd.merge(newdf1, newdf2, left_index=True, right_index=True, how='outer', indicator=True))
