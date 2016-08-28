#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on 2016年8月27日

@author: duang
'''

key_test={'key':'a Test','key':'new Test'}
print key_test

NASDAQ_code={
    'BIDU':'Baidu',
    'SINA':'Sina',
    'YOKU':'Youku'
    }
print NASDAQ_code
NASDAQ_code['add']='Youku2'#add
print NASDAQ_code
NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})#add all
print NASDAQ_code
del NASDAQ_code['add']
print NASDAQ_code