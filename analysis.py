import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = 'd:\\subdata.xlsx'
xls = pd.ExcelFile(filename)
data = xls.parse('2020-10-16', dtype='object')
# data = data.drop('节点名称', axis=1)
print(data.head())
data['变化值'] = data['温度(℃)'].shift(1) - data['温度(℃)']
# data['时间'] = pd.to_datetime(data['时间'])
# data['时间'] = pd.datetime.strptime(data['时间'], '%H:%M:%S')
print(data.head())
print(data.dtypes)


# 超出特定温度，红色标记
def plot1(x, y, thresh):
    higher = np.ma.masked_where(y <= thresh, y)
    plt.plot(x, y, c='g')
    plt.plot(x, higher, c='r')
    plt.show()


# 变化异常，红色标记
def plot2(x, y, thresh):
    wencha = y.shift(1) - y
    higher = np.ma.masked_where(wencha <= thresh, y)
    plt.plot(x, y, c='g')
    plt.plot(x, higher, c='r')
    plt.show()


# def plot(x, y, thresh):
#     y_diff = np.copy(y)
#     for i in range(1, len(y)):
#         y_diff[i] = y[i] - y[i - 1]
#     y_diff = np.abs(y_diff)
#     higher = np.ma.masked_where(y_diff < thresh, y)
#     for i in range(0, len(higher)):
#         if higher[i] is not np.ma.masked:
#             higher[i - 1] = y[i - 1]
#     plt.plot(x, y, c='g')
#     plt.plot(x, higher, c='r')
#     plt.show()

# 最高温度mt
mt = data['温度(℃)'].astype(float).max()
print(mt)
# 最高温度的索引index
index = data['温度(℃)'].astype(float).idxmax()
print(index)
y = data['温度(℃)'][index]
x = data['时间'][index]
print(x, type(x))
print(y, type(y))


plt.xticks(range(0, 287, 64))
plt.title('Temperature exceed 30 degrees')
plt.ylabel('Temperature(℃)')
plt.xlabel('Time')
plot1(data['时间'], data['温度(℃)'], 30)

plt.xticks(range(0, 287, 64))
plt.title('The temperature change is more than 1 degree')
plt.ylabel('Temperature(℃)')
plt.xlabel('Time')
plot2(data['时间'], data['温度(℃)'], 0.1)

plt.xticks(range(0, 287, 64))
plt.ylabel('Temperature(℃)')
plt.xlabel('Time')
plt.plot(data['时间'], data['温度(℃)'], 'b-')
plt.annotate('max=' + str(mt)+'  time='+str(x), xy=(x, y), xytext=(x,y+2),
             arrowprops=dict(facecolor='black', shrink=0.1, width=2))
plt.show()
