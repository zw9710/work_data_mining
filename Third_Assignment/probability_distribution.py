# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:31:56 2020

@author: zw
"""
import numpy as np

"""以变量a为例求解"""
a = np.random.randint(0,10,100)    #范围内的整数
print(a)
np.mean(a)
np.median(a)
np.var(a)
np.std(a)


b=np.random.rand(40)    #0到1的均匀分布
print(b)
c=np.random.randn(10)    #标准正态分布
print(c)
d=np.random.normal(0,1,100)   #生成指定正态分布
print(d)
e=np.random.random(20)   #0到1的均匀分布
print(e)
f=np.random.ranf(20)   #0到1的均匀分布
print(f)
g=np.random.uniform(-1,1,100)   #指定均匀分布
print(g)