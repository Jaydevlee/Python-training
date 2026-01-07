import pandas

myindex = ['마포구', '용산구', '서대문구', '동대문구', '은평구', '구로구', '강서구']
mylist = [40, 80, 70, 50, 60, 30, 20]
myseries = pandas.Series(data = mylist, index = myindex)

print(myseries)
print('-' * 40)
print(myseries.loc['은평구'])
print('-' * 40)
print(myseries.loc['서대문구' : '구로구'])
print('-' * 40)
print(myseries.loc['용산구' : '동대문구'])
print('-' * 40)
print(myseries.iloc[1])
print('-' * 40)
print(myseries.iloc[0:5:2])
print('-' * 40)
print(myseries.iloc[[1, 3, 4]])
print('-' * 40)
print(myseries.iloc[2:5])
print('-' * 40)
myseries.iloc[2] = 99
myseries.iloc[2:5] = 66
myseries.loc[['마포구', '강서구']] = 55
myseries.iloc[0::2] = 77
print('-' * 40)
print(myseries)