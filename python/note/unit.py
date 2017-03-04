#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月27日
@author: duang
'''
import time
a_list = range(0,10)
print sum(a_list)
b_list=[2,1,3]
print sum(b_list)
print sorted(b_list,reverse=True)
print b_list
c_list=[4,5,6]
for b,c in zip(b_list,c_list):
    print(b,'is',c)

t0=time.clock()
a=[]
for i in range(1,11):
    a.append(i)
t1=time.clock()
print a,range(1,11),t1-t0
t0=time.clock()
b=[i*2 for i in range(1,11)]#推导式 列表解析式 list comprehension
t1=time.clock()
print b,t1-t0
letters=['a','b','c','d']
for num,letter in enumerate(letters):
    print (letter,'index is',num)