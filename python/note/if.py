#!/usr/bin/python
# -*- coding:utf-8 -*-
def account_login():
    password = input('password :')
    #print password,password==123
    if password==123:
        print 'login success!'
    elif password in '123':
        print 'like'
    else:
        print 'Wrong password or invalid input!'
        account_login()
        
account_login()    