#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月27日

@author: duang
'''
print 1 > 2 # False
print 1 < 2 <3 # True
print 42 != '42' # True
print 'Name' == 'name' # False
print 'M' in 'Magic' # True
number = 12
print number is 12 # True
print 1<number<10 #False 多条件比较

print 42 == 'the answer' #False 不同类型只能用== ！=
print 42 != 'the answer' #True

print True > False #True
print True + False > False + False#True
print bool(0)+bool([])+bool('')+bool(False)+bool(None)#False

#in is   
album = ['Black Star','David Bowie',25,True]
album.append('new song')
print 'Black Star' in album#True
album2=album
print album is album2#true

#and && or ||