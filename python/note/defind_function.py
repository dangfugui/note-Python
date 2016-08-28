#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月27日

@author: duang
'''
def add(a,b):
    return a+b

def fahrenheit_converter(C):
    fahrenheit = C * 9/5 + 32
    return str(fahrenheit) +'˚F'

def trapezoid_area(base_up, base_down, height=1):#默认参数
    return ((base_down+base_up)/2)*height


print add(1,2)
print fahrenheit_converter(35)
print trapezoid_area(1,2,3)#位置参数
print trapezoid_area(1,2)#使用默认参数height
print trapezoid_area(base_up=1, base_down=2, height=3)#关键词传输
print trapezoid_area(1, base_down=2, height=3)#混合
