#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月27日

@author: duang
'''
#string
name='My name is Mike'
print name[0]#M 
print name[-4]#M 倒数第四个
print name[11:14]#Mik
print name[11:15]#Mike
print name[5:]#me is Mike 
print name[:5]#My na
index='0123456789-9876543210'
print index[-1]#0
phone_number="183-1097-7758"
hiding_number=phone_number.replace(phone_number[:9],'*'*9)
print hiding_number
print phone_number.find('-')
print('{} a word she can get what she {} for.'.format('With','came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))



