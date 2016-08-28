#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月27日

@author: duang
'''
from _ast import Num
items=[1,2,3,4]
for item in items:
    print item
    
for num in range(1,11):#range 左开右闭
    print num
    
for i in range(1,10):
    for j in range(1,10):
        print ('{} X {} = {}'.format(i,j,i*j))
        
        
while i>0:
    if i%2==0:
        print 'i='+str(i)
    i=i-1
    