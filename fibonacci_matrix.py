# -*- coding: utf-8 -*-
"""
This is a file that USES a circular statement to find the Fibonacci sequence.

Created on Wed Oct 28 20:30:40 2020

@author: zw

software: Spyder 4.1.5

"""
import numpy as np    #引入numpy模块
print ("Welcome to use this program to calculate Fibonacci series.")
print ("------------------------------------------------------------")
num_input= input ("Please input positive number:") 
if not num_input.isdigit () :    #利用isdigit()判断输入内容是否为正整数，若不是发出警告！
    print ("\033[1;31mPlease input positive number again!\033[0m")
    num_input = input ("Please input positive number:") 
fib_num=int(num_input)
def fibonacci_matrix(n):    #定义矩阵函数
    res = pow((np.mat([[1, 1], [1, 0]])), n) * np.mat([[1], [0]]) #使用mat方法直接定义矩阵
    return res[0][0] 
for i in range(fib_num):
    print(int(fibonacci_matrix(i)), end=' ')    #输出矩阵中对应位置数值
print('\n')
