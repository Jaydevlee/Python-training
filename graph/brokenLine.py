import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family = 'Malgun Gothic')
cnt, PNG, UNDERBAR=0, '.png', '_'
CHART_NAME = 'brokenLine'
filename = './data/주요발생국가주간동향(4월2째주).csv'

data = pd.read_csv(filename, index_col='국가')
chartdata = data['4월06일']
print(chartdata)

plt.plot(chartdata, color='blue', linestyle='solid', marker='o')

YTICKS_INTERVAL = 50000
maxlim = (int(chartdata.max() / YTICKS_INTERVAL) + 1) * YTICKS_INTERVAL
values = np.arange(0, maxlim + 1, YTICKS_INTERVAL)
plt.yticks(values, ['%s' % format(val, ',') for val in values])

plt.grid(True)
plt.xlabel('국가명')
plt.ylabel('발생 건수')
plt.title('4월 6일 코로나 발생 건수')

cnt += 1
savefile = CHART_NAME + UNDERBAR +str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일이 저장되었습니다.')