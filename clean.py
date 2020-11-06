import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
filename = 'D:\\data.xlsx'
xls = pd.ExcelFile(filename)
data = xls.parse('Sheet1', dtype='object')

# 查看前五行
print(data.head())
print(data.shape)  # (1629, 3)
# print(data.dtypes)
# 节点名称             object
# 温度(℃)            object
# 记录时间     datetime64[ns]
# dtype: object


# 数据清洗
# step1：选择子集，只留第二第三列
subdata = data.loc[:, '温度(℃)':'记录时间']
# print(type(subdata))
# print(subdata.head())


# step2：缺失数据处理
# 观察数据，发现，有部分行缺失数据
print('删除缺失值前大小', subdata.shape)
subdata = subdata.dropna(subset=['温度(℃)'])
print('删除缺失值后大小', subdata.shape)

# step3：数据类型转换
# 一开始我们导入的表格中所有的数据都是按字符串类型导入的，现在需要将温度改为数值类型
subdata['温度(℃)'] = subdata['温度(℃)'].astype('float')
print('转换后的数据类型：\n', subdata.dtypes)

# 转换后的数据类型：
#  温度(℃)           float64
# 记录时间     datetime64[ns]
# dtype: object

# 我们的记录时间已经是datatime类型，无需转换
# 无需数据排序，数据已经按照采集时间依次排列了

# step4：异常值处理

subdata.to_excel('D:\\cleandata.xlsx')


# 按时间列拆分表格

# 将记录时间拆分为日期和时间两列
def splitRecordtime(timeStemp):
    dataList = []  # 存放日期
    timeList = []  # 存放时间
    for value in timeStemp:
        timeStr = value.strftime('%Y-%m-%d %H:%M:%S')  # 将timestemp类型转化为string类型
        dataList.append(timeStr.split(' ')[0])  # 提取日期
        timeList.append(timeStr.split(' ')[1])  # 提取时间

    dataSer = pd.Series(dataList)
    timeSer = pd.Series(timeList)
    return dataSer, timeSer


timelist = subdata.loc[:, '记录时间']  # 获取记录时间这一列
print(timelist.shape)
dataSer, timeSer = splitRecordtime(timelist)  # 对字符串进行分割，获得日期和时间
subdata['日期'] = dataSer
subdata['时间'] = timeSer
subdata = subdata.drop('记录时间', axis=1)

print(subdata.head())
print(subdata.shape)
print(subdata.describe())

# 将清洗完的数据保存
subdata.to_excel('D:\\subdata.xlsx')
