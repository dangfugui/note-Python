#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月28日
@author: duang
'''
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plot
class MyMatplotlib_pyplot():
    def gaussian_distribution(self):#绘图5.1 绘制正态分布概率密度函数
        mu=0
        sigma=1
        x=np.linspace(mu-3*sigma,mu+3*sigma,50)
        y=np.exp(-(x-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma)
        print(x)
        print(y)
        plot.plot(x,y,'r-',x,y,'go',linewidth=2,markersize=8)
        plot.grid(True)
        plot.show()
    def logistic(self):#损失函数：Logistic损失(-1,1)/SVM Hinge损失/ 0/1损失
        x=np.linspace(-3,3,100)
        y_logit=np.log(1+np.exp(-x))/np.log(2)
        y_1=x<0
        y_hinge=1-x
        y_hinge[y_hinge<0]=0
        plot.plot(x,y_logit,'r-', label='Logistic Loss', linewidth=2)
        plot.plot(x,y_1,'g-', label='0/1 Loss',linewidth=2)
        plot.plot(x,y_hinge, label='Hinge Loss',linewidth=2)
        plot.grid()
        plot.legend(loc='upper right')
        plot.show()
        
        
if __name__ == '__main__':
    mycm=MyMatplotlib_pyplot()
    #mycm.gaussian_distribution()#绘制正态分布概率密度函数
    mycm.logistic()#损失函数：Logistic损失(-1,1)/SVM Hinge损失/ 0/1损失