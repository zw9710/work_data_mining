# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 00:28:28 2020

@author: zw
"""

#这是一个猜数字游戏。1-100之间数字猜测
import random #引入模块
rand_num = random.randint(1,100)    #产生1到100的随机数，整数型数字
print ('--------欢迎您来到猜数字游戏-------')
count = 0     #初始化猜测次数
while (True):     #构造While循环
    guess = input("这个数字是1到100间的整数，请输入您的猜测值:")    #希望游戏体验者输入0到100的数字
    count += 1
    if not guess.isdigit():
        print ("请输入1到100间的整数！")
        continue
    elif int(guess) > 100 or int(guess) < 1:
        print("请再次确定您输入的是1到100间的数字!")
        continue
    elif int(guess) > rand_num:
        print('你猜的数太高了！')
    elif int(guess) < rand_num:
        print('你猜的数太低了！')
    else :
        print(f'聪明的您猜对了呢!您一共猜了{count}次!这个数字是{rand_num}')
        break

    