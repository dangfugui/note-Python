#!/usr/bin/python
# -*- coding:utf-8 -*-
import numpy
from PIL import Image
from numpy import *
import os
import os.path

class VerifyCode:
    infected_pixels_list = []  # 这个专门用来存放每一次感染的点的List
    character_list = []  # 用于存放切割出来的字符
    trainingSetList = []
    img = [[]]
    def __init__(self,basePath,critical):
        self.basePath =basePath
        self.critical = critical  # 临界值
        basePath = basePath[:-4]

    def saveImg(self, path):
        Image.fromarray(self.img).save(path)

    # 感染算法
    def start_infectiomn(self,path):
        # 使用PIL打开一个图片转换成L模式，即灰阶模式，并转换成array对象
        self.img = array(Image.open(path).convert('L').point(lambda x: 255 if x > self.critical else 0))
        infection_point = len(self.img) / 4  # 感染点甚至为图片垂直方向正中间
        for i in range(len(self.img[infection_point])):  # 感染点甚至为图片垂直方向正中间
            if self.img[infection_point, i] == 0:  # 发现黑色像素
                self.infected_pixels_list = []
                self.virus_infection( infection_point, i)  # 调用病毒感染递归方法
                min_x = 999
                min_y = 999
                for i in self.infected_pixels_list:
                    if i[0] < min_x:
                        min_x = i[0]
                    if i[1] < min_y:
                        min_y = i[1]
                    revise_infected_pixels_list = []
                for i in self.infected_pixels_list:
                    revise = [0,0]
                    revise[0] = i[0] - min_x + 1
                    revise[1] = i[1] - min_y + 1
                    revise_infected_pixels_list.append(revise)
                newImg = array(Image.new('L', (12, 18)).point(lambda x: 255))
                for i in revise_infected_pixels_list:
                    newImg[i[0], i[1]] = 0
                self.character_list.append(newImg)  # 把整个字符的所有点存在list中
        return self.character_list

    # 感染算法
    def virus_infection(self,row, col):  # 病毒感染：用递归方法来遍历当前像素点相邻的8个点
        img = self.img
        if row < len(img) and col < len(img[0]) and img[row][col] < self.critical:
            self.infected_pixels_list.append((row, col))
            img[row][col] = 255;
            self.virus_infection( row - 1, col - 1)
            self.virus_infection( row - 1, col + 1)
            self.virus_infection( row - 1, col)
            self.virus_infection( row, col - 1)
            self.virus_infection( row, col + 1)
            self.virus_infection( row + 1, col - 1)
            self.virus_infection( row + 1, col + 1)
            self.virus_infection( row + 1, col)

    #打印分割成标准化的图片
    def print_normalized(self):
        index = 0
        for item in self.character_list:
            newImg = array(Image.new( 'L',(12,18)).point(lambda x:255))
            for i in item:
                newImg[i[0],i[1]] = 0
            Image.fromarray(newImg).save(self.basePath+'2_'+str(index)+'.jpg')
            index = index + 1

    #KNN（K-Nearest Neighbor，“K最近邻”
    def learnKNN(self,sign):
        for parent, dirnames, filenames in os.walk(self.basePath):
            for filename in filenames:
                if sign !=filename[0]:
                    break
                fileFullPath = os.path.join(parent,filename)
                img = array(Image.open(fileFullPath).convert('L').point(lambda x: 255 if x > self.critical else 0))
                self.trainingSetList.append([filename,img])

    #和拆分的图片计算欧式距离  对比距离返回结果
    def predict(self,img):
        distanceList = []
        #img = array(Image.open(file).convert('L').point(lambda x:255 if x>100 else 0))
        for i in self.trainingSetList:  #遍历样本数据，和需要识别的图片算距离
            trainingFileName = i[0]
            trainingImg = i[1]
            distance = self.getDistance(img,trainingImg)             #调用计算距离的方法，得到两张图片的欧氏距离
            distanceList.append([trainingFileName,distance])         #把样本名和距离存到一个新的集合里
        distanceList.sort(lambda x,y:cmp(x[1],y[1]))            #对集合按照距离进行排序
        return distanceList[0][0]


    def getDistance(self ,sourceImg,trainingImg):
        distance = 0
        for i in range(len(trainingImg)):
            for j in range(len(trainingImg[0])):
                distance +=((int(sourceImg[i][j]) - int(trainingImg[i][j]))**2)     #numpy.linalg.norm(vec1-vec2)
        return distance
        # return numpy.linalg.norm(sourceImg - trainingImg)


if __name__ == '__main__':
    # 归一化数据
    # for parent, dirnames, filenames in os.walk('codeImg'):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    #     for fileName in filenames:  # 输出文件夹信息
    #         basePath = parent + '/' + fileName
    #         verify = VerifyCode(basePath, 138)  # 去噪
    #         Image.fromarray(verify.img).save(basePath[:-4] + '1.jpg')  # 保存去噪的图像
    #         verify.start_infectiomn()  # 感染分割法
    #         verify.print_normalized()  # 保存分割后的图像  手动打标
    verify = VerifyCode('codeImg',138)  # 去噪
    verify.learnKNN('L')
    charList = verify.start_infectiomn('codeImg/verifyCodeF0.jpg')
    for charArray in charList :
        print verify.predict(charArray)




