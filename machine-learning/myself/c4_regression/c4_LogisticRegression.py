#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月30日

@author: duang
'''
import csv
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing.data import StandardScaler

class LogisticRegression_my():
    def __init__(self):#初始化
        self.linearRegression_lris(True)
   
    def readFile(self):
        path=u'..\\..\\..\\data\\machine-learning-4\\4.iris.data'
#         #手动读文件
#         f=file(path)
#         x=[]
#         y=[]
#         for d in f:
#             d=d.strip()
#             if d:
#                 d=d.split(',')
#                 y.append(d[-1])
#                 x.append(map(float,d[:-1]))
#         print x,y
#         x=np.array(x)
#         y=np.array(y)
#         y[y=='Iris-setosa']=0
#         y[y=='Iris-versicolor']=1
#         y[y=='Iris-virginica']=2
#         print x,y
        
#         df=pd.read_csv(path)
#         x=df.values[:,:-1]
#         y=df.values[:,-1]
#         print x,y
#         le=preprocessing.LabelEncoder()
        # 路径，浮点型数据，逗号分隔，第4列使用函数iris_type单独处理
        def iris_type(s):
            it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
            return it[s]
        data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
        #print data
        # 将数据的0到3列组成x，第4列得到y
        x, y = np.split(data, (4,), axis=1)#axis 0是按行切 1是按照列分
        return x,y
    def linearRegression_lris(self,forview=False):
        x,y=self.readFile()
        # 为了可视化，仅使用前两列特征
        if forview:
#             x = x[:, :2]
            x = x[:,(1,3)]
        #x=StandardScaler().fit_transform(x)#标准化  #这个做了不好
        logreg = LogisticRegression()   # Logistic回归模型
        logreg.fit(x, y.ravel())        # 根据数据[x,y]，计算回归参数

        # 画图
        N, M = 500, 500     # 横纵各采样多少个值
        x1_min, x1_max = x[:, 0].min(), x[:, 0].max()   # 第0列的范围
        x2_min, x2_max = x[:, 1].min(), x[:, 1].max()   # 第1列的范围
        t1 = np.linspace(x1_min, x1_max, N)
        t2 = np.linspace(x2_min, x2_max, M)
        x1, x2 = np.meshgrid(t1, t2)                    # 生成网格采样点
        x_test = np.stack((x1.flat, x2.flat), axis=1)   # 测试点
        print t1
        print t2
        print x_test
        if forview==False:
        # 无意义，只是为了凑另外两个维度
            x3 = np.ones(x1.size) * np.average(x[:, 2])
            x4 = np.ones(x1.size) * np.average(x[:, 3])
            x_test = np.stack((x1.flat, x2.flat, x3, x4), axis=1)  # 测试点
    
        y_hat = logreg.predict(x_test)                  # 预测值
        y_hat = y_hat.reshape(x1.shape)                 # 使之与输入的形状相同
        plt.pcolormesh(x1, x2, y_hat,cmap=plt.cm.Spectral, alpha=0.1)  # 预测值的显示Paired/Spectral/coolwarm/summer/spring/OrRd/Oranges
        plt.scatter(x[:, 0], x[:, 1],c=y, edgecolors='k', s=50, cmap=plt.cm.prism)  # 样本的显示  s 圈的大小
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.xlim(x1_min, x1_max)
        plt.ylim(x2_min, x2_max)
        plt.grid()
        plt.show()
        
        # 训练集上的预测结果
        y_hat = logreg.predict(x)
        y = y.reshape(-1)       # 此转置仅仅为了print时能够集中显示
        print y_hat.shape       # 不妨显示下y_hat的形状
        print y.shape
        result = (y_hat == y)   # True则预测正确，False则预测错误
        print y_hat
        print y
        print result
        c = np.count_nonzero(result)    # 统计预测正确的个数
        print c,len(result)
        print 'Accuracy: %.2f%%' % (100 * float(c) / float(len(result)))

        

        
if __name__ == '__main__':
    a=LogisticRegression_my();
