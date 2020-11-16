# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:11:13 2020

@author: zw

software: Spyder 4.1.5

"""
num_input=int(input("请输入1到3999的数字："))
class Solution:    #定义类Solution
    """
    阿拉伯数字实例化，输出罗马字符
    """ 
    def __init__(self,num) :    #初始化函数，引入属性num和roman
        self.num = num
        self.roman = ""
    def __iter__(self) :
        return self
    def __next__(self) :
        if self.num > 3999 or self.num < 1 :
            print("请输入1到3999之间的数字")
            return self.num
        else:
            num_tuple = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            roman_tuple = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
            for i in range(len(num_tuple)):
                while self.num >= num_tuple[i]:
                    self.num -= num_tuple[i]
                    self.roman += roman_tuple[i]
            return self.roman  
if __name__ == '__main__' :
    s=Solution(num_input)    
    print(s.__next__())
                     