import matplotlib.pyplot as plt
import pandas as pd

# 读取清洗完的数据
filename = 'D:\\cleandata.xlsx'
xls = pd.ExcelFile(filename)
cleandata = xls.parse('Sheet1', dtype='object')

plt.plot(cleandata['记录时间'], cleandata['温度(℃)'], 'b-')
plt.show()


