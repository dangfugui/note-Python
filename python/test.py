#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年9月2日

@author: dang
'''

def getAns(n):
    up = 1;
    ans = 1;
    d = 2;
    while True:
        if (d > n):
            break;
        if((d + up) <= (n + 1)):
            ans += up
            d += up
            up=up+1
        else:
            ans += (n - d + 1);
            break;
        if(d <= n):
            ans=ans-1
            d=d+1
    return ans
while True:
    n = int(raw_input())
    print getAns(n)
