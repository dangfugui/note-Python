#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月28日
@author: duang
'''
import numpy as np
import time
import math
from astropy.io.votable.converters import Bit

# numpy是非常好用的数据包，如：可以这样得到这个二维数组
class MyNumpy():
    def array(self):#list数组
        list_a=[1,2,3,4,5,6]
        print("lsit_a=",list_a,type(list_a))
        ndarray_a=np.array(list_a)
        print('np_array=',ndarray_a,type(ndarray_a),ndarray_a.shape)
        ndarray_b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]);
        print('ndarray_b=',ndarray_b,type(ndarray_b))
        print(ndarray_b.shape)
        ndarray_b.shape=2,-1
        print ndarray_b
        c=ndarray_b.reshape((4,-1))
        print(c)
        print c.dtype
        d=np.array([1,2,3],dtype=np.float)
        f=np.array([1,2,3],dtype=np.complex)#复数类型
        print(d,d.dtype)
        print(f,f.dtype)
        #a=np.arange(0,60,10).reshape((-1,1))+np.arange(6)
        #print('a=', a,type(a))
    
    def space(self):#等差等比
        a=np.arange(1,10,0.5)#1到10 间隔是0.5 等差为0.5
        print(a)
        b=np.linspace(1,10,10)#1到10 取5个数  False右闭
        print(b)
        c=np.linspace(1,10,10,endpoint=False)#1到10 取5个数  False右开
        print(c)
        d=np.logspace(1, 2, 20, endpoint=True) #10^1到10^2 取20个等比数
        print(d)
        f=np.logspace(0,10,11,endpoint=True,base=2)# 创建起始值为2^0，终止值为2^10(包括)，有11个数的等比数列
        print(f)
    
    def section(self):#切片
        a=np.arange(10)
        print(a)
        print(a[1])
        print(a[3:6])#3,4,5 左开右闭
        print(a[2:])
        print(a[1:9:2])
        print(a[::-1])
        a[1:3]=11,22
        a[3]=333
        print(a)
        b=a[5:]
        b[0]=555
        print(a)
        print(b)
        bit=np.logspace(0, 9, 10, base=2)
        print (bit)
        index=np.arange(0,10,2)
        print (index)
        bit2=bit[index]
        print(bit2)
        bit2[2]=100
        print(bit)
        print(bit2)
        rand=np.random.rand(10)
        print (rand)
        print(rand>0.5)
        bool=rand[rand>0.5]
        print(bool)
        rand[rand>0.5]=0.5
        print(rand)
        
    def mapArray(self):#形状 #二维数组和切片
        a=np.arange(0,50,10)
        print (a)
        b=a.reshape((-1,1))
        print(b)
        c=np.arange(6)
        print(c)
        f=b+c #行+列
        print(f)
        like=np.linspace(0,50,6,dtype=np.int).reshape((-1,1))+np.arange(6)
        print(like)
        print('like[(0,1,2,3),(2,3,4,5)]')
        print(like[(0,1,2,3),(2,3,4,5)])
        print(like[3:,(0,2,5)])
        bool=np.array([True,False,True,False,True,False])
        print(like[bool])
        print(like[bool,3])
        
    def time(self):#numpy和python的运算效率对比
        for j in np.logspace(0,7,10):
            j=int(j)
            x=np.linspace(0,10,j)
            start=time.clock()
            y=np.sin(x)
            t1=time.clock()-start
            x2=x.tolist()
            start=time.clock()
            for i,t in enumerate(x2):
                x[i]=math.sin(t)
            t2=time.clock()-start
            print j,':',t1,t2,t2/t1
        
    
if __name__ == '__main__':
    myNumpy=MyNumpy()
    # myNumpy.array()#数组
    #myNumpy.space()#等差等比
    #myNumpy.section()#切片
    #myNumpy.mapArray()#形状 二维数组和切片
    myNumpy.time()#numpy和python的运算效率对比