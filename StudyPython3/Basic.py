#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:24:04 2017

@author: cooperlink 
"""

# #号开头的行，为注释行
"""
多行注释使用 
 \""" 多行注释的能容 \"""
 斜线符号 \ 用来转义字符
"""  

a = 10
if a > 0: # 以 : 号结束的语句下面缩进的语句为其代码块, 缩进的代码复制粘贴后将不再缩进
    print(a)
    print('a =', a)
else:
    print(-a)

    
    
## 数据类型

# 整数
print(2, -2) #十进制
print(0b10, -0b10) #二进制
print(0xe, -0xe) #十六进制


# 浮点数
print(3.14, -3.14)
print(1200, '=', 1.2e3) #科学计数法 e 代表 10
print(0.00314, '=', 3.14e-3)


# 字符串

#字符串是使用 "" 或 '' 括起来的文本
#一些特殊字符 要使用 \ 进行转义
print('I\'m Python3', '=', "I\'m Python3")
print('There is \n Python3')
print('\\\n\\')
print(r'\\\n\\', r"\\\n\\") # r'' 和 r"" 表示其内的字符不转义

#多行字符使用 ''' ''' , r''' '''表示不转义其内字符
str = r'''line1 
line2 \n
line3'''
print(str)




# 布尔值 True, False
print(True, False)
print(4 < 5)

#布尔值使用 and、or 和 not 运算
print(True and True)
print(True and False)
print(False and False)


print(True or True)
print(True or False)
print(False or False)

print(not True)
print(not False)

print(1 < 2 and 2 < 3)
print(not 3 < 4)

# if 和 布尔值
if 4 < 9:
    print('4 < 9')
else:
    print('4 > 9')
    

# 空值使用 None 表示, None 不是 0，而是一个特殊的空值
print(None)




# 变量

#变量名必须是大小写英文、数字和_的组合，且不能用数字开头
a = 10 # a 是整数
a = 'ABC' # a 是字符串
a = True # a 是布尔值

# = 是赋值的意思
x = 10 
print('x = ', x)
x = x + 10
print('x = ', x)




# 常量
# Python习惯使用全大写的变量名表示常量，事实并不是常量，依然可以改变
PI = 3.1415926 
PI = 4




# 除号 / 的结果永远是浮点数， 要想结果为整数要使用 //
# 只用整数使用 // 或 % 时结果才是整数
print(9/4)
print(9/3)
print(9//4)
print(9//3)

print(9.1//3) #浮点数还是浮点数

print(5%2)
print(5%2.1)






