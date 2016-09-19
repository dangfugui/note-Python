#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年9月12日
@author: dang
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from matplotlib.pyplot import axis
from docutils.utils.math.math2html import LineWriter

class DecisionTreeIris:
    # 花萼长度、花萼宽度，花瓣长度，花瓣宽度
    iris_feature = 'sepal length', 'sepal width', 'petal length', 'petal width'
    def __init__(self):
        x,y=self.get_data()
        self.create_tree(x,y)
    def iris_type(self,s):
        it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
        return it[s]
        
    def get_data(self):
        path=u'..\\..\\..\\data\\machine-learning-4\\4.iris.data'
        data = np.loadtxt(path,dtype=float,delimiter=',',converters={4:self.iris_type})
        #print data
        x,y=np.split(data,(4,),axis=1) # 将数据的0到3列组成x，第4列得到y
        #print 'x=\n' ,x
        x = x[:, :2] # 为了可视化，仅使用前两列特征 第一个冒号是每行全要  :2 代表只要0,1列
        return x,y;
         
    def create_tree(self,x,y):
        # 决策树参数估计
        # min_samples_split = 10：如果该结点包含的样本数目大于10，则(有可能)对其分支
        # min_samples_leaf = 10：若将某结点分支后，得到的每个子结点样本数目都大于10，则完成分支；否则，不进行分支
        clf = DecisionTreeClassifier(criterion='entropy', max_depth=30, min_samples_leaf=3) #entropy熵
        dt_clf = clf.fit(x, y)
        
        #画图
        N,M=50,50#横纵各采样多少个值
        x1_min,x1_max=x[:,0].min(),x[:,0].max()#第0列范围
        x2_min,x2_max=x[:,1].min(),x[:,1].max()#第1列范围
        t1=np.linspace(x1_min,x1_max,N)
        t2=np.linspace(x2_min,x2_max,M)
        x1,x2=np.meshgrid(t1,t2)#生成网格采样点
        x_test=np.stack((x1.flat, x2.flat),  axis=1)#测试点
        y_hat=dt_clf.predict(x_test)#预测值
        y_hat=y_hat.reshape(x1.shape)#使与输入的形状相同
        print y_hat
        plt.pcolormesh(x1, x2, y_hat, cmap=plt.cm.Spectral, alpha=0.1)  # 预测值的显示Paired/Spectral/coolwarm/summer/spring/OrRd/Oranges
#         plt.plot(x1,x2,'go',label='x1,x2',Linewidth=2,alpha=0.8);
#         plt.plot(x_test[:,0:1],x_test[:,1:2],'r^',label='x1,x2',Linewidth=2,alpha=0.8);
        plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', cmap=plt.cm.prism)  # 样本的显示
        plt.xlabel(self.iris_feature[0])
        plt.ylabel(self.iris_feature[1])
        plt.xlim(x1_min, x1_max)
        plt.ylim(x2_min, x2_max)
        plt.grid()
        plt.show()
        # 训练集上的预测结果
        y_hat = dt_clf.predict(x)
        y = y.reshape(-1)       # 此转置仅仅为了print时能够集中显示
        print y_hat.shape       # 不妨显示下y_hat的形状
        print y.shape
        result = (y_hat == y)   # True则预测正确，False则预测错误
        print y_hat
        print y
        print result
        c = np.count_nonzero(result)    # 统计预测正确的个数
        print c
        print 'Accuracy: %.2f%%' % (100 * float(c) / float(len(result)))
            
        
        
        
if __name__ == '__main__':
    dec=DecisionTreeIris()