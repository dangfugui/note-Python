#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月27日

@author: duang
'''
def add(a,b):
    return a+b

all_in_list=[
    1,                  #整数
    1.11,               #浮点数
    'a word',           #字符串
    True,               #布尔值
    ['list1','list2'],  #列表中套列表
    (1,2),              #元组
    {'key':'value'},    #字典
    add(1,2)            #函数 3
    ]
print all_in_list

list=['Monday','Tuesday','Wednesday','Thursday','Friday']
print list
list.insert(1, 'one')
print list
list[0:0]=['0range']
print list
list[2]='two'
list.remove('0range')
print list
del list[0:2]
print list