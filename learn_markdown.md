1.`#`的个数表示几级**标题**，例如一级标题#+一个空格

# 一级标题

## 二级标题

---

2.段落的话直接编写

---

3.可用三个`-`或者`_`或者`*`来显示一条**分割线**

---

4.可用两个<kbd>*</kbd>或者__来**加粗**字体<kbd>helllo</kbd>

**加粗**

__加粗__

---

5.可用一个*来表示**斜体** 

*斜体*

_斜体_

---

6.可用三个*或者__表示**粗斜体**

***粗斜体***

___粗斜体___

---

7.用两个~表示**删除线**

~~删除~~

---

8.用<和>来表示**自动连接**

<http://baidu.com>

---

9.**内部连接**

[](),中括号里面写标题，圆括号里面写连接名称

[baidu](http://baidu.com)

---

10.**链接标题**

[]()圆括号的最后在双引号里面写入标题,鼠标悬停在连接上，有一个工具提示

[baidu](http://baidu.com "baidu")

---

11.命名锚点，能跳转到同一页面的指定锚点

---

12.**插入图像**

与连接类似，但前面多一个感叹号()里面可以加入本地照片的地址，也可以是网页地址

<img src="file:///d:/zhujing2.jpg" title="" alt="Mart Text" width="224">

<img src="https://c-ssl.duitang.com/uploads/item/202007/15/20200715132614_biuub.jpg" title="" alt="头像" width="242">

---

13.**引用**

在引用的文字前加入向右的尖括号`>`,还支持嵌套，用两个，三个括号,记得括号后面加空格才生效

> 引用>
> 
> > 嵌套
> > 
> > > 再嵌套
> > > 
> > > 

---

14.**列表**

无序的，可用*或者-或者+放在最前面,可嵌套

* *valide bullet 
- -valid bullet
+ +valid bullet
  
  + 嵌套

有序的，用数字加.再加空格，按回车，自己生成序号

1. first

2. second

如果已经写好了内容，需要序号，一个个重新排序比较麻烦，可以直接在要排序的内容最前面全部填1.和空格就行了

1. first

2. second

---

15.**代办事项列表**

用-加空格加[ ]加空格就行啦，刚输入-和空格时变成无序列表的符号，不用管继续输入[ ]就行，记得[]中间是有空格的

- [x] task1

- [ ] job2

---

16.**表格** 

通过在每个单元格之间使用|来创建表，在标题下方加入一行-来分隔,好吧现在不需要了，回车直接创建好了，可以直接resize table来调整表格大小

| name | age |
|:----:|:---:|
|      |     |

-----

17.**对其单元格** 

可以轻触表格就会在顶部出现对其方式，一般都是直接调整光标所在位置的一列

| name    | age |
|:-------:|:---:|
| polaris | 19  |

---

18.**内部代码**

使用反引号`,切换到英文模式，左上角就是

`hello world`

---

19.**代码块**

用三个连续的反引号然后再输入你写的代码所用的语言

```python
int a
a=0
print(a)
```

---

20.**缩进代码**

连续四个空格就是这个效果，但一般不用，因为没有上面那么好读，也没有语法突出

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code

---

21.**显示成键盘键的样子**

用`<kbd>`和`</kbd>`组合使用

to copy,please press <kbd>ctrl</kbd>+<kbd>+</kbd>

----

22.**表情**

冒号中间夹着表情名称heart,zap,cow,dollar,star,tada

:heart:

:zap:

:cherry_blossom:

---

22.**数学公式**

用美元符号`$`去包裹一行

For example, to show $\alpha \beta \gamma$ inline with other text, just wrap it in dollar signs.

---

23.**数学公式块**

用`$$`在所有公式的前后

$$
m=\frac{b_y-a_y}{b_x-a_x}
$$



$$
R_x=\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & cos(a) & -sin(a) & 0\\
0 & sin(a) & cos(a) & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
$$

---

24.图

```vega-lite
{
  "data": {
    "values": [
      {"a": "C", "b": 2}, {"a": "C", "b": 7}, {"a": "C", "b": 4},
      {"a": "D", "b": 1}, {"a": "D", "b": 2}, {"a": "D", "b": 6},
      {"a": "E", "b": 8}, {"a": "E", "b": 4}, {"a": "E", "b": 7}
    ]
  },
  "mark": "point",
  "encoding": {
    "x": {"field": "a", "type": "nominal"},
    "y": {"field": "b", "type": "quantitative"}
  }
}
```

```flowchart
st=>start: Start|past
e=>end: End|future
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Yes
or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|future

st->op1(right)->cond
cond(yes, right)->c2
cond(no)->sub1(left)->op1
c2(yes)->io->e
c2(no)->op2->e
```

---

24.反斜杠

任何一个标识符都可以用反斜杠

\*这不是一个用来斜体\*


