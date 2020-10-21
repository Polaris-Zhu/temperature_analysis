import pandas as pd
import numpy as np

# series类型
# # 直接由列表创建
# a = pd.Series([9, 8, 7, 6])  # 直接由列表创建
# print(a)
#
# # 自定义索引
# b = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
# print(b)
#
# # 由字典来创建series
# d = pd.Series({'a':9, 'b':8, 'c':7})
# print(d)
#
# # 可以用index修改索引，注意d对应NaN
# e = pd.Series({'a':9,'b':8, 'c':7},index=['c','a','b','d'])
# print(e)
#
# # series类型也可以直接由numpy中的ndarray类型创建
# import numpy as np
# n = pd.Series(np.arange(5))
# print(n)
#
# # 同时可以用index特定索引
# m = pd.Series(np.arange(5), index=np.arange(9,4,-1))
# print(m)
#
# print(b)
# print(b.index)  # 获得索引
# print(b.values)  # 获得数据
# # 注意，自动索引和自定义索引并存
# print(b['b'])
# print(b[1])
# # print(b['b', 'c', 0])   两种索引方式不能混合使用
#
# # 单个索引返回的是值，切片索引返回的是series类型
# print(b[3])
# print(b[:3])
#
# # 对series运算返回的结果同样是series类型
# print(b[b > b.median()])  # median函数用来返回中值
# print(np.exp(b))   #exp函数返回以e为底的指数函数。即e的x次方
#
# print(b.get('f', 100))
# # get（）用于获取f对应的值，如果没有则返回100

# series + series
# a = pd.Series([1, 2, 3], ['c', 'd', 'e'])
# b = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])
# print(a + b)
# Series类型在运算过程中会自动对齐不同索引的数据 没有对齐的数据不会做计算，返回NaN

# Series对象和索引都可以有一个名字，存储在属性.name中
# print(b.name)
# b.name = 'Series对象'
# b.index.name = '索引列'
# print(b)

# 简而言之，Series类型就是一个一维d带索引的数组


# DataFrame类型
# DataFrame类型就是Pandas库的二维数据类型，多列数据共用一套索引
# DataFrame是一个表格型的数据类型，每列值类型可以不同，DataFrame既有行索引、也有列索引
# DataFrame常用于表达二维数据，但可以表达多维数据


# 可以由二维ndarray对象创建DataFrame类型
# d = pd.DataFrame(np.arange(10).reshape(2, 5))
# print(d)
#    0  1  2  3  4
# 0  0  1  2  3  4
# 1  5  6  7  8  9  行和列上都会自动生成索引

# 一维ndarray对象/列表可以通过字典类型生成DataFrame类型
# dt = {'one':pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#        'two':pd.Series([9,8,7,6],index=['a','b','c','d'])}
# d=pd.DataFrame(dt)
# print(d)
#    one  two  <---自定义列索引
# a  1.0    9
# b  2.0    8
# c  3.0    7
# d  NaN    6
# ^---自定义行索引

# e = pd.DataFrame(dt, index=['b', 'c', 'd'], columns=['two', 'three'])  # index表示行索引，columns表示列索引
# print(e)
#    two three
# b    8   NaN
# c    7   NaN
# d    6   NaN    数据根据行列索引自动补全，没有的数据NaN

d1 = {'城市': ['北京', '上海', '广州', '深圳', '沈阳'],
      '环比': [100, 101, 102, 103, 101],
      '同比': [120, 103, 110, 121, 123]}
d = pd.DataFrame(d1, index=['c1', 'c2', 'c3', 'c4', 'c5'])
print(d)
#     城市   环比   同比
# c1  北京  100  120
# c2  上海  101  103
# c3  广州  102  110
# c4  深圳  103  121
# c5  沈阳  101  123
print(d['同比'])
# c1    120
# c2    103
# c3    110
# c4    121
# c5    123
# Name: 同比, dtype: int64
print(d[1:2])
# c2  上海  101  103  左闭右开
print(d.iloc[-1])
# 城市     沈阳
# 环比    101
# 同比    123
# Name: c5, dtype: object  选取最后一行，返回Series 一维
print(d.iloc[-1:])
#  城市   环比   同比
# c5  沈阳  101  123   选取最后一行，返回DataFrame 二维
print(d['同比']['c2'])
# 103   先列后行


# 数据类型操作
# .reindex()能够改变或重排Series和DataFrame（标出index还是colums）索引
# d = d.reindex(index=['c5', 'c4', 'c3', 'c2', 'c1'])
# print(d)
#     城市   环比   同比
# c5  沈阳  101  123
# c4  深圳  103  121
# c3  广州  102  110
# c2  上海  101  103
# c1  北京  100  120
# d = d.reindex(columns=['城市', '同比', '环比'])
# print(d)
#     城市   同比   环比
# c5  沈阳  123  101
# c4  深圳  121  103
# c3  广州  110  102
# c2  上海  103  101
# c1  北京  120  100
#
# newc = d.columns.insert(2,'新增')  #第一个参数为要插入的位置，第二个为列命
# newd = d.reindex(columns=newc, fill_value=200)
# print(newd)
#     城市   同比   新增   环比
# c5  沈阳  123  200  101
# c4  深圳  121  200  103
# c3  广州  110  200  102
# c2  上海  103  200  101
# c1  北京  120  200  100

# nc = d.columns.delete(2)  # 删除第三列位置的数
# ni = d.index.insert(5, 'c0')  #在第六行增加一行c0
# nd = d.reindex(index=ni, columns=nc).ffill()  # ffill当前值向前填充，bfill向后填充
# print(nd)
#     城市     同比
# c5  沈阳  123.0
# c4  深圳  121.0
# c3  广州  110.0
# c2  上海  103.0
# c1  北京  120.0
# c0  北京  120.0

# .drop()能够删除Series和DataFrame指定行或列索引
# a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
# print(a)
# a    9
# b    8
# c    7
# d    6
# dtype: int64

# a1 = a.drop(['b', 'c'])  # 有返回值，不能直接a.drop(),这样的话，a没变
# print(a1)
# a    9
# d    6
# dtype: int64

# 删除方法DataFrame.drop(labels=None,axis=0, index=None, columns=None, inplace=False)
# print(d)
#     城市   同比   环比
# c5  沈阳  123  101
# c4  深圳  121  103
# c3  广州  110  102
# c2  上海  103  101
# c1  北京  120  100
# d1 = d.drop('c5')   # 删除c5行
# print(d1)
#     城市   同比   环比
# c4  深圳  121  103
# c3  广州  110  102
# c2  上海  103  101
# c1  北京  120  100

# d2 = d.drop('同比', axis=1)
# print(d2)
#     城市   环比
# c5  沈阳  101
# c4  深圳  103
# c3  广州  102
# c2  上海  101
# c1  北京  100


# pandas库数据类型计算
a = pd.DataFrame(np.arange(12).reshape(3, 4))
print(a)
b = pd.DataFrame(np.arange(20).reshape(4, 5))
print(b)
print(b.add(a, fill_value=100))  # b+a fill_value参数代替NaN，替代后参与运算
print(a.mul(b, fill_value=0))  # a*b fill_value参数代替NaN，代替后参与运算
# .add(d, **argws) 加法  .sub(d, **argws) 减法   .mul(d, **argws) 乘法   .div(d, **argws) 除法

# 不同维度之间的运算为广播运算
# 轴用来为超过一维数组定义的属性，二维数据拥有两个轴：第0轴沿着行的方向垂直向下，第1轴沿着列的方向水平延申。
# 根据官方的说法，1表示横轴，方向从左到右；0表示纵轴，方向从上到下。当axis=1时，数组的变化是横向的，体现出列的增加或者减少。
# 反之，当axis=0时，数组的变化是纵向的，体现出行的增加或减少。
# 一维Series默认在轴1参与运算
c = pd.Series(np.arange(4))
print(c)
print(c - 10)
print(b - 1)
print(b - c)
print(b.sub(c, axis=0))  # 使用运算方法可以令一维Series参与轴0运算

# 排序
#  .sort_index()方法在指定轴上根据索引进行排序，默认升序
# .sort_index(axis=0,ascending=True)默认按行索引排序，默认升序
d = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
print(d)
print(d.sort_index())
print(d.sort_index(ascending=False))
# .sort_values(by, axis=0, ascending=True)
# 在指定轴上根据数值进行排序，默认升序
print(d.sort_values(2, ascending=False))  # 按第三列降序排序
print(d.sort_values('a', axis=1, ascending=False))  # 按‘a’行降序排序
# NaN统一放到排序末尾

# 统计分析函数
# 适用于Series和DataFrame类型
# .sum() 计算数据的总和，按0轴计算，下同
# .count() 非NaN值的数量
# .mean()   .median() 计算数据的算数平均值、算数中位数
# .var() .std()  计算数据的方差、标准差
# .min()  .max()  计算数据的最小值、最大值

# 适用于Series类型
# .argmin() .argmax() 计算数据的最大值、最小值所在位置的索引位置（自动索引）
# idxmin()  .idxmax()  计算数据最大值、最小值所在位置的索引（自定义索引）

# .describe()针对0轴（各列）的统计汇总，一次性输出多种统计数值
a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
print(a)
print(a.median())
print(a.describe())
# count    4.000000
# mean     7.500000
# std      1.290994
# min      6.000000
# 25%      6.750000
# 50%      7.500000
# 75%      8.250000
# max      9.000000
# dtype: float64

print(type(a.describe()))
# <class 'pandas.core.series.Series'>

print(d.describe())
print(type(b.describe()))
# <class 'pandas.core.frame.DataFrame'>

# 数据类型为Series和DataFrame，所以可以使用索引
print(a.describe()['max'])

# print(d.describe().ix['max'])

print(d.describe()[0])  # 打印第一列
# count     4.000000
# mean      7.500000
# std       6.454972
# min       0.000000
# 25%       3.750000
# 50%       7.500000
# 75%      11.250000
# max      15.000000
# Name: 0, dtype: float64

print(d.describe().iloc[1, [0]])  # 打印第二行第一列
# 0    7.5
# Name: mean, dtype: float64

print(d.describe().loc[['max'], :])
# 如果想选取一列，只能使用.loc[,] 第一个参数为行，第二个为列

# 累计分析：对前1-N个数进行累加  纵向上
# 适用于Series和Dataframe类型，累计计算
# .cumsum()  依次给出前1，2...n个数的和
# .cumprod()  依次给出前1，2...n个数的积
# .cummax()   依次给出前1，2...n个数的最大值
# .cummin()   依次给出前1，2...n个数的最小值


b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
print(b)
#     0   1   2   3   4
# c   0   1   2   3   4
# a   5   6   7   8   9
# d  10  11  12  13  14
# b  15  16  17  18  19

print(b.cumsum())
#     0   1   2   3   4
# c   0   1   2   3   4
# a   5   7   9  11  13
# d  15  18  21  24  27
# b  30  34  38  42  46
print(b.cumprod())
#    0     1     2     3     4
# # c  0     1     2     3     4
# # a  0     6    14    24    36
# # d  0    66   168   312   504
# # b  0  1056  2856  5616  9576
print(b.cummax())
#     0   1   2   3   4
# c   0   1   2   3   4
# a   5   6   7   8   9
# d  10  11  12  13  14
# b  15  16  17  18  19
print(b.cummin())
#    0  1  2  3  4
# c  0  1  2  3  4
# a  0  1  2  3  4
# d  0  1  2  3  4
# b  0  1  2  3  4

# 滚动/窗口计算函数：依次计算相邻x个元素
# 适用Series和DataFrame类型，滚动计算（窗口计算）
# .rolling(w).sum()  依次计算相邻w个元素的和
# .rolling(w).mean()  依次计算相邻w个元素的算数平均值
# .rolling(w).var()  依次计算相邻w个元素的方差
# .rolling(w).std()  依次计算相邻w个元素的标准差
# .rolling(w).min()  .;max()  依次计算相邻w个元素的最大值和最小值

print(b.rolling(2).sum())  # 纵向上以两个元素为单位进行求和运算
#       0     1     2     3     4
# c   NaN   NaN   NaN   NaN   NaN
# a   5.0   7.0   9.0  11.0  13.0
# d  15.0  17.0  19.0  21.0  23.0
# b  25.0  27.0  29.0  31.0  33.0
print(b.rolling(3).sum())  # 纵向上以三个元素为单位进行求和运算
#      0     1     2     3     4
# c   NaN   NaN   NaN   NaN   NaN
# a   NaN   NaN   NaN   NaN   NaN
# d  15.0  18.0  21.0  24.0  27.0
# b  30.0  33.0  36.0  39.0  42.0


# 相关性分析
# 相关性最基本的就是：
# • X增大，Y增大，两个变量正相关
# • X增大，Y减小，两个变量负相关
# • X增大，Y无视，两个变量不相

# 分析相关性的方法：

# 1.协方差  cov(X,Y)
# >0,X和Y正相关
# <0,X和Y负相关
# =0,X和Y独立无关

# 2.Pearson相关系数 (r的取值范围[-1,1])
# 0.8-1.0 极强相关
# 0.6-0.8 强相关
# 0.4-0.6 中等程度相关
# 0.2-0.4 弱相关
# 0.0-0.2 极弱相关或无相关
# 适用于Series和DataFrame类型
# .cov()  计算协方差矩阵
# .corr() 计算相关系数矩阵，Pearson，Spearman，Kendall等系数

hprice = pd.Series([3.04, 22.93, 12.75, 22.6, 12.33], index=['2008', '2009', '2010', '2011', '2012'])
m2 = pd.Series([8.18, 18.38, 9.13, 7.82, 6.69], index=['2008', '2009', '2010', '2011', '2012'])
print(hprice.corr(m2))
# 0.5239439145220387
# 得出结论 中等程度相关
