# https://zhuanlan.zhihu.com/p/37025609
import numpy as np
import matplotlib

# 1.Matplotlib简介
# Matplotlib库由各种可视化类构成，内部结构复杂。
# matplotlib.pyplot是绘制各种可视化图形的命令子库，相当于快捷方式

# 2.图形绘制plt.plot
import matplotlib.pyplot as plt

# plt.plot([3, 1, 4, 5, 2])  # 输入一个含5个元素的列表
# plt.ylabel('grade')  # 定义y轴为‘gread’
# plt.savefig('test', dpi=600)  # 输出文件，文件名为‘test’
# plt.show()  # 显示图形

# plt.plot()中输入一维列表或数组时，其数值为y轴上的数，x轴上的数自动对应其索引
# plt.savefig()将输出图形存储为文件，默认PNG格式，通过dpi修改输出质量

# plt.plot([0, 2, 4, 6, 8], [1, 5, 4, 6, 2])
# plt.ylabel('grade')
# plt.axis([-1, 10, 0, 6])  # x轴为-1到10，y轴为0到6
# plt.show()

# plot.plot(x,y)中x列表为x轴上的数，y列表为对应x轴位置上y轴的数
# plot.axis()参数一定为一个四元素列表，前两个数为x轴左右范围，后两个为y轴上下范围

# 3.pyplot的绘图区域
# plt.subplot(nrows,ncols,plot_number)是最简单的分割绘图区域的方法
# nrows：横轴数量
# ncols：纵轴数量
# plot_number:当前绘图区域
# plt.subplot(3, 2, 4)


# def f(t):  # 定义一个能量衰减函数
#     return np.exp(-t) * np.cos(2 * np.pi * t)  # 调用numpy中的exp和cos函数
#
#
# def g(t):
#     return np.cos(2 * np.pi * t)
#
#
# a = np.arange(0.0, 5.0, 0.02)  # 使用numpy生成一个数组a，0.0到5.0之间每隔0.02生成一个数
# plt.subplot(2, 1, 1)  # 生成一个2个横轴的绘图区域，打开一个绘图区域
# plt.plot(a, f(a))  # 横轴为a，纵轴为f(a)
#
# plt.subplot(2, 1, 2)  # 打开第二个绘图区域
# plt.plot(a, g(a), 'r--')  # 横轴为a，纵轴为g(a),'r--'表示用虚线画
# plt.show()

# 4.使用plt.plot()绘制多条曲线
# a = np.arange(10)
# plt.plot(a, a * 1.5, 'b''.', a, a * 2.5, 'g--d', a, a * 3.5, 'm:x', a, a * 4.5, 'c-<')
# plt.show()

# 可以增加更多的关键字参数来修改每一个参数
# plt.plot(x,y,format_string,**kwargs)
# **kwargs 第二组或更多（x,y,format_string)
# color :控制颜色，color='green'
# linestyle：线条风格，linestyle='dashed'
# marker: 标记风格，marker='o'
# markerfacecolor:标记颜色，markerfacecolor='blue'
# markersize:标记尺寸，markersize=20

# 5.pyplot中的中文显示
# pyplot并不支持中文显示，可采取以下方法显示中文：
# 方法一、用rcParams修改字体
# matplotlib.rcParams['font.family'] = 'SimHei'  # 使用'SimHei'字体，即中文的黑体
# plt.plot([3, 1, 4, 5, 2])
# plt.ylabel('纵轴（值）')
# plt.savefig('test', dpi=600)
# plt.show()

# font.family 用于显示字体的名字
# font.style 字体风格，正常'normal'或斜体'italic'
# font.size 字体大小，整数字号或者'large'、'x-small'
# 基本中文字体种类：
# 'SimHei' 中文黑体
# 'Kaiti' 中文楷体
# 'LiSu' 中文隶书
# 'FangSong' 中文仿宋
# 'YouYuan' 中文幼圆
# 'STSong' 华文宋体

# matplotlib.rcParams['font.family'] = 'SimHei'  # 字体为宋体
# matplotlib.rcParams['font.size'] = 20  # 字号为20

# a = np.arange(0.0, 5.0, 0.02)
# plt.xlabel('横轴：时间')
# plt.ylabel('纵轴：振幅')
# plt.plot(a, np.cos(2 * np.pi * a), 'r--')
# plt.show()

# 方法二：在有中文输出的地方，增加一个属性：fontproperties
# a = np.arange(0.0, 5.0, 0.02)
# plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=20)
# plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=20)
# plt.plot(a, np.cos(a*np.pi*2),'r--')
# plt.show()

# 这种方法只对局部需要中文的地方进行修改，不影响整体


# 6.pyplot的文本显示
# plt.xlabel() 对x轴增加文本标签
# plt.xlabel() 对x轴增加文本标签
# plt.title() 对图形整体增加文本标签
# plt.text() 在任意位置增加文本
# plt.annotata() 在图形中增加带箭头的注解

# 例题：
# a = np.arange(0.0, 5.0, 0.02)
# plt.plot(a, np.cos(a * np.pi * 2), 'r--')
# plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15)
# plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
# plt.title(r'正弦波实例$y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
# plt.text(2, 1, r'$\mu=100$', fontsize=15)
# matplotlib.pyplot.text(x, y, s, fontdict=None, withdash=False, **kwargs)
# 通过函数方式，向axes对象添加text对象，确切的说是向axes的(x,y)位置添加s文本。返回一个text实例。

# plt.axis([-1, 6, -2, 2])
# plt.grid(True)
# plt.show()


# 文本显示还有一种函数：plt.annotate(s, xy=arrow_crd, xytext=text_crd, arrowprops=dict)
# s：要注解的字符串
# xy：箭头所在的位置
# xytext：文本显示的位置
# arrowprops：字典类型，定义整个箭头显示的一些属性

# a = np.arange(0.0, 5.0, 0.02)
# plt.plot(a, np.cos(a * np.pi * 2), 'r--')
# plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15)
# plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
# plt.title(r'正弦波实例$y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
# plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1, width=2))
# shrink设置为0.1，使箭头和(2,1)位置有一些距离。
# plt.axis([-1, 6, -2, 2])
# plt.grid(True)
# plt.show()

# matplotlib.pyplot.grid(b, which, axis, color, linestyle, linewidth， **kwargs)
#  b : 布尔值。就是是否显示网格线的意思。官网说如果b设置为None， 且kwargs长度为0，则切换网格状态。
#  which : 取值为'major', 'minor'， 'both'。 默认为'major'。
#  axis : 取值为‘both’， ‘x’，‘y’。就是想绘制哪个方向的网格线。
# color : 这就不用多说了，就是设置网格线的颜色。或者直接用c来代替color也可以。
# linestyle :也可以用ls来代替linestyle， 设置网格线的风格，是连续实线，虚线或者其它不同的线条。 | '-' | '--'                        | '-.' | ':' | 'None' | '' | '']
#  linewidth : 设置网格线的宽度


# 7.pyplot子绘图区域的设计方法
# 仅仅使用subplot方法是不行的，需要使用plt.subplot2grid()来辅助完成。
# plt.subplot2grid(GridSpec, CurSpec, colspan=1, rowspan=1)
from matplotlib import gridspec

# plt.subplot2grid((3, 3), (0, 0), colspan=3)  # 对应ax1
# plt.subplot2grid((3, 3), (1, 0), colspan=2)  # 对应ax2
# # （3,3）意味着将整块区域分为三行三列共九个区域，（1,0）意味着选纵向第二横向第1个区域（ax2的左半边），colspan=2意味着长度为2。
# plt.subplot2grid((3, 3), (1, 2), rowspan=2)  # 对应ax3
# plt.subplot2grid((3, 3), (2, 0))  # 对应ax4
# plt.subplot2grid((3, 3), (2, 1))  # 对应ax5

# 也可以这么写
# gs = gridspec.GridSpec(3, 3)
#
# ax1 = plt.subplot(gs[0, :])
# ax2 = plt.subplot(gs[1, :2])
# ax3 = plt.subplot(gs[1:, 2])
# ax4 = plt.subplot(gs[2, 0])
# ax5 = plt.subplot(gs[2, 1])
# plt.show()


# 8.常用的pyplot图标函数
# 使用matplotlib库我们最重要的是找最合适的可视化方法
# plt.plot(x,y,fmt...) 绘制一个坐标图
# plt.boxplot(data,notch,position) 绘制一个箱型图
# plt.bar(left,height,width,bottom) 绘制一个条形图
# plt.bath(width,bottom,left,height) 绘制一个横向条形图
# plt.polar(theta,r) 绘制极坐标图
# plt.pie(data,explode) 绘制饼图

# plt.psd(x,NFFT=256,pad_to,Fs) 绘制功率谱密度图
# plt.specgram(x,NFFT=256,pad_to,F) 绘制谱图
# plt.cohere(x,y,NFFT=256,Fs) 绘制X-Y的相关性函数
# plt.scatter(x,y) 绘制散点图，其中，x和y长度相同
# plt.step(x,y,where) 绘制步阶图
# plt.hist(x,bins,normed) 绘制直方图

# plt.contour(X,Y,Z,N) 绘制等值图
# plt.vlines() 绘制垂直图
# plt.stem(s,y,linefmt,markerfmt) 绘制柴火图
# plt.plot_date() 绘制数据日期

# 例题
# 饼图
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'  # 设置每个标签的名称
# sizes = [15, 30, 45, 10]  # 设置每个标签的比例
# explode = (0, 0.1, 0, 0)  # 将第二块突出出来，突出程度为0.1
# plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# plt.show()
# autopct表示百分数的表示方法
# shadow为False时为无阴影二维饼图，为True时是有阴影的
# startangle表示饼图起始的角度
# 我们现在修改下，将图片绘制为标准的圆形：
# plt.axis('equal')

# 直方图
# np.random.sample(0)  # 设置一个随机种子0
# mu, sigma = 100, 20  # 均值为100，方差为20
# a = np.random.normal(mu, sigma, size=100)  # 生成数组a
# plt.hist(a, 20, histtype='stepfilled', facecolor='b', alpha=0.75)
# plt.title('Histogram')  # 设置标题名称
# plt.show()

# a为数组a
# 20为直方的个数，改成10或40的结果如下：
# histtype为直方图的类型，facecolor为颜色，alpha为透明度


# 极坐标图
# 这里我们采用面向对象的方法绘制

# N = 20  # 极坐标图中数据的个数为20
# theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)  # 从0到360°（2*π）等分出N个不同的角度
# radii = 10 * np.random.rand(N)  # 随机生成每个角度对应的值
# width = np.pi / 4 * np.random.rand(N)  # 设置每个值的宽度
# np.random.rand(N)意为在[0,1)之间随机生成N个数。
# ax = plt.subplot(111, projection='polar')  # 生成一个绘图区域，projection设为极坐标图
# bars = ax.bar(theta, radii, width=width, bottom=0.0)  # theta对应left，radii对应hight，width对应width
# for r, bar in zip(radii, bars):
#     bar.set_facecolor(plt.cm.viridis(r / 10.))
#     bar.set_alpha(0.5)
# plt.show()


# 散点图
fig, ax = plt.subplots()  # 生成一个绘图区域
ax.plot(10 * np.random.randn(100), 10 * np.random.randn(100), 'o')
ax.set_title('Simple Scatter')
plt.show()
# ax为当前绘图区域绘图对象
# ‘o’为实心圆点。