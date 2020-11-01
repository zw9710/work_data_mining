# 关于Python内置对象类型“列表”的综述
---
**By:ZW**

本章节我们重点学习一种关于Python内置对象类型——列表（list)。列表在Python中具有非常强大的功能！

## 1.列表的基本知识和应用特点
---

定义：在Python中，常用方括号表示一个列表——[].

### 1.1 列表所装对象的类型

在方括号内，可以是数字（包括浮点数和整数），也可以是字符串，还可以是True/False这样的布尔值，或者其他类型的对象，甚至是多种不同类型的对象。

我们可以先定义一个空列表：

```
>>> a=[]    #定义空列表
>>> type(a)    #使用type()查看变量a所指向对象的类型
<class 'list'>
>>> bool(a)    #判断对象是“真”还是“假”
False
>>> print(a)    #利用print()函数输出
[]
```
再来看一个非空列表：
```
>>> a=['2',3,'qiwsir.github.io']
>>> a
['2', 3, 'qiwsir.github.io']
>>> type(a)
<class 'list'>
>>> bool(a)
True
>>> print(a)
['2', 3, 'qiwsir.github.io']
```
可以看到列表所装对象是不确定的，应了那句“列表是个筐，什么都能装”。
### 1.2 索引和切片
```
>>> ur1="qiwsir.github.io"
>>> ur1[2]    #查询ur1列表第3位元素，python的第一位元素索引为0
‘w’
>>> ur1[:4]    #查询ur1列表前四个元素
'qiws'
>>> ur1[3:9]    #查询url列表第4位到第9位元素
'sir.gi'
>>> a=['2',3,'qiwsir.github,io']
>>> a[1:]     #查询a列表从第2位元素开始之后的所有元素
[3, 'qiwsir.github,io']
>>> a[1:2]
[3]
>>> a[2][7:13]#对a列表元素进行二次切片
'github'
#输出的结果意思是先输出a列表的第三位元素'qiwsir.github,io'，然后把该元素作为列表，输出第8位到14位的元素。
```
列表中的索引和切片，与字符串是一样的。
```
>>> lang="python"
>>> lang.index("y")
1
>>> lst=['python','java','c++']#从右边开始编号，-1就是右边第一个
>>> lst[-1]
'c++'
>>> lang[-1:-3]
''
>>> lang[-3:-1]
'ho'
```
### 1.3 反转
```
>>> alst=[1,2,3,4,5,6]
>>> alst[::-1]
[6, 5, 4, 3, 2, 1]
>>> alst[::1]#c此处表示步长为1，从左开始每个一个字符选取一个字符
[1, 2, 3, 4, 5, 6]
>>> alst[::2]#此处表示步长为从左开始每隔2选取一个字符
[1, 3, 5]
#这里也可以用reversed()反转
>>> list(reversed(alst))
[6, 5, 4, 3, 2, 1]
```
### 1.4 操作
1）len()

```
>>> lst=['python','java','c++']#求取列表的长度
>>> len(lst)
3
```
2)"+"连接两个序列
```
>>> lst=['python','java','c++']#+号是直接将两个元素之间连接起来，不是对应元素相加
>>> alst=[1,2,3,4,5,6]
>>> lst+alst
['python', 'java', 'c++', 1, 2, 3, 4, 5, 6]
```
3）“*”重复序列元素
```
>>> lst*3#*也同样是将对应的字符串连接起来
['python', 'java', 'c++', 'python', 'java', 'c++', 'python', 'java', 'c++']
```
4)in
```
>>> "python" in lst
True
>>> "c#" in lst
False
```
5)max/min
```
>>> max(alst)
6
>>> min(alst)
1
>>> max(lst)
'python'
>>> min(lst)
'c++'
```
### 1.5 修改列表元素
```
>>> cities=["nanjing","zhenjiang"]#直接赋值，将镇江改为苏州
>>> cities[1]="suzhou"
>>> cities
['nanjing', 'suzhou']
>>> cities.append("shanghai")#append函数可以追加元素
>>> cities
['nanjing', 'suzhou', 'shanghai']
```
### 1.6 列表函数
1）append/extend
```
>>> la=[1,2,3]
>>> lb=['qiwsir','python']#extend可以将两个表合并
>>> la.extend(lb)
>>> la
[1, 2, 3, 'qiwsir', 'python']
#append在上文已经阐释，此处不做解释
```
2）count
```
>>> la=[1,2,1,1,3]
>>> la.count(1)
3
```
3)index
```
>>> la=[1,2,3,'a','b','c','qiwsir','python']
>>> la.index(3)#检测3在该数组中第一次出现的位置
2
```
4)inset
```
>>> all_users=['qiwsir','github','io']
>>> all_users.insert(0,"python")
>>> all_users
['python', 'qiwsir', 'github', 'io']
```
5)remove/pop
```
>>> all_users=['python','http://','github','io','algorithm']
>>> all_users.remove("http://")#remove表示从该列表中移除
>>> all_users
['python', 'github', 'io', 'algorithm']
>>> all_users.pop(1)#指定删除编号为1的元素
'github'
```
6)reverse
```
a=[3,5,1,6]
a.reverse()
a
```
7)sort
```
>>> a=[6,1,5,3]
>>> a.sort()
>>> a
[1, 3, 5, 6]
```
## 2.列表和元组的异同

### 1）列表list与数组array的定义：

a)列表是由一系列按特定顺序排列的元素组成，可以将任何东西加入列表中，其中的元素之间没有任何关系；

b)Python中的列表(list)用于顺序存储结构。它可以方便、高效的的添加删除元素，并且列表中的元素可以是多种类型。

c)数组也就是一个同一类型的数据的有限集合。

### 2)列表list与数组array的相同点：

都可以根据索引来取其中的元素

### 3)列表list与数组array的不同点：

a)列表list中的元素的数据类型可以不一样。数组array里的元素的数据类型必须一样；

b)列表list不可以进行数学四则运算，数组array可以进行数学四则运算；

c)相对于array，列表会使用更多的存储空间。





