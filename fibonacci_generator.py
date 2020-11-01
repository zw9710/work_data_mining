# -*- coding: utf-8 -*-
"""
This is a file that uses generator to find the Fibonacci sequence.

Created on Wed Oct 28 20:00:40 2020

@author: zw

software: Spyder 4.1.5

"""
print ("Welcome to use this program to calculate Fibonacci series.")
print ("------------------------------------------------------------")
num_input = input ("Please input positive number:") 
if not num_input.isdigit() :    #利用isdigit()判断输入内容是否为正整数，若不是发出警告！
    print ("\033[1;31mPlease input positive number again!\033[0m") 
    num_input = input ("Please input positive number :") 
fib_num = int(num_input)    #将字符串转化为整数
fib_list = []   #创建空列表
def fibonacci_generator(n) : 
    a ,b  = 1 , 1
    i=1 
    while i <= n : 
        yield a 
        a , b = b , a + b
        i += 1
if __name__ == '__main__':     #调用函数求数列
    fib = fibonacci_generator(fib_num)
for index in fib:
    fib_list.append(index)
print (fib_list)