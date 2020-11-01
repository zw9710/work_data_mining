# -*- coding: utf-8 -*-
"""
This is a file that uses iterator to find the Fibonacci sequence.

Created on Wed Oct 28 20:30:40 2020

@author: zw

software: Spyder 4.1.5

"""
print ("Welcome to use this program to calculate Fibonacci series.")
print ("------------------------------------------------------------")
num_input= input ("Please input positive number:") 
if not num_input.isdigit () :    #利用isdigit()判断输入内容是否为正整数，若不是发出警告！
    print ("\033[1;31mPlease input positive number again!\033[0m")
    num_input = input ("Please input positive number:") 
fib_num=int(num_input)
fib_list = []
class Fibonacci_iterator(object):    #创建Fibonacci类
    def __init__(self, n):  
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1
    def __next__(self):
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration
    def __iter__(self):
        return self
if __name__ == '__main__':   #调用
    fib = Fibonacci_iterator(fib_num)
    for index in fib:
        fib_list.append(index)
print (fib_list)