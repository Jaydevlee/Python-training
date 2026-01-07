import pandas as pd
import numpy as np

myindex = ['김구', '이봉창', '안중근', '윤봉길']
mycolumns = ['강남구', '은평구', '마포구', '용산구']
mylist = list(10 * onedata for onedata in range(1,17))
myframe = pd.DataFrame(np.reshape(mylist, (4, 4)), index=myindex, columns=mycolumns)
print(myframe.iloc[0])
print('-' * 40)
print(myframe.iloc[[0, 2]])
print('-' * 40)
print(myframe.loc['윤봉길'])
print('-' * 40)
print(myframe.loc[['이봉창', '윤봉길']])
print('-' * 40)
print(myframe.loc[['윤봉길'], ['은평구']])
print('-' * 40)
print(myframe.loc[['김구', '이봉창'], ['용산구','은평구']])
print('-' * 40)
print(myframe.loc[myframe['은평구'] <= 100])
print('-' * 40)
print(myframe.loc[myframe['은평구'] == 100])
print('-' * 40)
myframe.loc['김구' : '안중근', ['용산구']] = 80
print(myframe)
