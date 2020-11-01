# -*- coding: utf-8 -*-
"""
This is a file that uses loop to find the Fibonacci sequence.

Created on Wed Oct 28 18:00:40 2020

@author: zw

software: Spyder 4.1.5

"""
print ("Welcome to use this program to calculate Fibonacci series.")    #说明语
print ("------------------------------------------------------------")
num_input = input ("Please input positive number:") 
if not num_input.isdigit() :    #利用isdigit()判断输入内容是否为正整数，若不是发出警告！
    print ("\033[1;31mPlease input positive number again!\033[0m")
    num_input = input ("Please input positive number:") 
fib_num = int(num_input)    #利用int()函数将字符串转换为整数
def fibonacci_loop(n):    #定义Fibonacci循环函数
    fib_list = []
    a, b = 0, 1
    while n > 0:
        fib_list.append(b)
        a, b = b, a + b
        n-=1
    return fib_list
if __name__ == '__main__':    #调用函数求数列
    fib = fibonacci_loop(fib_num)
print (fib)
      