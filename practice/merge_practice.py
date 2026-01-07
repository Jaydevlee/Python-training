import pandas as pd

dict1 = {"이름" : ['유관순', '유관순', '황진이', '황진이', '유관순'],
         "중간" : [10, 20, 30, 40, 50]}
df1 = pd.DataFrame(dict1)
print(df1)
print('-' * 40)
dict2 = {"이름" : ['황진이', '유관순', '심사임당'],
        "기말" : [30, 40, 50]}
df2 = pd.DataFrame(dict2)
print(df2)
print('-' * 40)
result1 = pd.merge(df1, df2, on='이름')
print(result1)
print('-' * 40)
result2 = pd.merge(df1, df2, on='이름', how = 'right')
print(result2)