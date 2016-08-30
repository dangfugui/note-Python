#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月30日

@author: duang
'''
import csv
import numpy as np
import pandas as pd#数据处理
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split#随机切分训练数据，测试数据
from sklearn.linear_model.base import LinearRegression#线性回归

class MLinearRegression():
    def __init__(self):#初始化
#         print self.readFile();#读文件
#         self.plotXY(data)#绘制原始图
        self.plotXY3()
        self.linearRegression_sales()
    def readFile(self,path):#读文件
        print path
        #Python自带库读取文件
#         f=file(path,'rb')
#         print f
#         data=csv.reader(f)
#         for line in data:
#             print line
#         f.close()

        #numpy读入
#         p=np.loadtxt(path,delimiter=',',skiprows=1)#逗号分隔，从第一行开始
#         print p
        
        # pandas读入
        data = pd.read_csv(path)    # TV、Radio、Newspaper、Sales
#         x = data[['TV', 'Radio', 'Newspaper']]
#         # x = data[['TV', 'Radio']]
#         y = data['Sales']
        return data
        
    def plotXY(self):#绘制原始图
        path=u'..\\..\\data\\machine-learning-4\\4.Advertising.csv'
        data=self.readFile(path);
        plt.plot(data['TV'],data['Sales'],'ro',label='TV')
        plt.plot(data['Radio'],data['Sales'],'g^',label='Radio')
        plt.plot(data['Newspaper'],data['Sales'],'mv',label='Newspaper')
        plt.legend(loc='lower right')
        plt.grid()
        plt.show()
    
    def plotXY3(self):#绘制原始对比图
        path=u'..\\..\\data\\machine-learning-4\\4.Advertising.csv'
        data=self.readFile(path);
        plt.figure(figsize=(9,12))#9*12英寸的图片
        plt.subplot(311)    #3行1列 绘制第1个
        plt.plot(data['TV'], data['Sales'], 'ro')
        plt.title('TV')
        plt.grid()
        plt.subplot(312)
        plt.plot(data['Radio'], data['Sales'], 'g^')
        plt.title('Radio')
        plt.grid()
        plt.subplot(313)
        plt.plot(data['Newspaper'], data['Sales'], 'b*')
        plt.title('Newspaper')
        plt.grid()
        plt.tight_layout()
        plt.show()
        
    def linearRegression_sales(self):#线性回归
        path=u'..\\..\\data\\machine-learning-4\\4.Advertising.csv'
        data=self.readFile(path);
#         x=data[['TV', 'Radio', 'Newspaper']]
        x=data[['TV', 'Radio']]
        y=data['Sales']
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
        # print x_train, y_train
        linreg = LinearRegression()
        model = linreg.fit(x_train, y_train)
        print model
        print linreg.coef_
        print linreg.intercept_
        y_hat=linreg.predict(np.array(x_test))
        mse=np.average((y_hat-y_test)**2)
        rmse=np.sqrt(mse)
        print mse,rmse
        
        t=np.arange(len(x_test))
        plt.plot(t,y_test,'r-',linewidth=2,label='Test')
        plt.plot(t,y_hat,'g-',linewidth=2,label='Predict')
        plt.grid()
        plt.legend(loc='upper right')
        plt.show()
        
   
if __name__ == '__main__':
    a=MLinearRegression();
