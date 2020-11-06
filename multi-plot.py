import pandas as pd
import matplotlib.pyplot as plt

# 读取每天的数据
filename = 'D:\\subdata.xlsx'
xls = pd.ExcelFile(filename)

day15 = xls.parse('2020-10-15', dtype='object')
day16 = xls.parse('2020-10-16', dtype='object')
day17 = xls.parse('2020-10-17', dtype='object')
day18 = xls.parse('2020-10-18', dtype='object')
day19 = xls.parse('2020-10-19', dtype='object')
day20 = xls.parse('2020-10-20', dtype='object')
day21 = xls.parse('2020-10-21', dtype='object')

# data = []
# data[0] = xls.parse('2020-10-16', dtype='object')
# data[1] = xls.parse('2020-10-16', dtype='object')
# data[2] = xls.parse('2020-10-16', dtype='object')
# data[3] = xls.parse('2020-10-16', dtype='object')

# for i in range(4):
#     # data[i] = xls.parse('2020-10-16', dtype='object')
#     plt.subplot(2, 2, i)
#     plt.plot(data[i]['时间'], data[i]['温度(℃)'], 'b-')
#     plt.xlabel('Time')
#     plt.ylabel('Temperature(℃)')
#     plt.title(data[i][])
#     plt.plot(data)
# 分别画图
plt.subplot(3, 2, 1)
plt.plot(day16['时间'], day16['温度(℃)'], 'b-')
plt.ylabel('Temperature(℃)')
plt.xlabel('Time')
plt.title('2020-10-16')
plt.xticks(range(0, 287, 64))

plt.subplot(3, 2, 2)
plt.plot(day17['时间'], day17['温度(℃)'], 'g-')
plt.ylabel('Temperature(℃)')
plt.xlabel('Time')
plt.title('2020-10-17')
plt.xticks(range(0, 287, 64))

plt.subplot(3, 2, 5)
plt.plot(day18['时间'], day18['温度(℃)'], 'r-')
plt.ylabel('Temperature(℃)')
plt.xlabel('Time')
plt.title('2020-10-18')
plt.xticks(range(0, 287, 64))

plt.subplot(3, 2, 6)
plt.plot(day19['时间'], day19['温度(℃)'], 'c-')
plt.ylabel('Temperature(℃)')
plt.xlabel('Time')
plt.title('2020-10-19')
plt.xticks(range(0, 287, 64))

# plt.subplot(3, 2, 5)
# plt.plot(day20['时间'], day20['温度(℃)'], 'b-')
# # plt.ylabel('Temperature(℃)')
# # plt.xlabel('Time')
# plt.title('2020-10-20')
# plt.xticks(range(0, 287, 64))

# plt.subplot(3, 2, 6)
# plt.plot(day21['时间'], day21['温度(℃)'], 'b-')
# plt.ylabel('Temperature(℃)')
# plt.xlabel('Time')
# plt.title('2020-10-21')
# plt.xticks(range(0, 287, 64))
plt.show()

# 选取16-19号做一个纵向对比
plt.plot(
    day16['时间'], day16['温度(℃)'], 'b-',
    day16['时间'], day17['温度(℃)'], 'g-',
    day16['时间'], day18['温度(℃)'], 'r-',
    day16['时间'], day19['温度(℃)'], 'c-')
plt.title('Temperature comparison from 16th to 19th')
plt.ylabel('Temperature(℃)')
plt.xlabel('Time')
plt.xticks(range(0, 287, 64))
plt.show()
