# coding=utf-8
import random
import matplotlib.pylab as plt
import numpy as np

# 解决中文输出
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

class Umatplotlib:
    '''
    绘图
    '''

    @staticmethod
    def scatter(sziea):
        '''
        散点图
        '''
        roll1_list = []
        roll2_list = []
        for i in range(sziea):
            roll1_list.append(random.randint(1, 6))
            roll2_list.append(random.randint(1, 6))
        x = range(1, sziea + 1)
        plt.scatter(x, roll1_list, alpha=0.5, c="red")
        plt.scatter(x, roll2_list, alpha=0.5, c="green")
        plt.show()

    @staticmethod
    def hist(size):
        roll_list = []
        for i in range(size):
            roll_list.append(random.randint(1, 6) + random.randint(1, 6))
        #   normed 归一化
        plt.hist(roll_list, range(2, 14), normed=1, edgecolor='black', linewidth=1)
        plt.title("骰子点统计")
        plt.xlabel("点数")
        plt.ylabel("频率")
        plt.show()

    @staticmethod
    def hist2(size):
        roll1_arr = np.random.randint(1, 7, size=size)
        roll2_arr = np.random.randint(1, 7, size=size)
        result_arr = roll1_arr + roll2_arr
        hist, bins = np.histogram(result_arr, bins=range(2, 14))
        print(hist)
        print(bins)
        #   normed 归一化
        plt.hist(result_arr, range(2, 14), normed=1, edgecolor='black', linewidth=1, rwidth=0.9)
        plt.xticks(np.arange(2, 13)+0.5, ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点'])
        plt.title("骰子点统计")
        plt.xlabel("点数")
        plt.ylabel("频率")
        plt.show()


if __name__ == '__main__':
    # Umatplotlib.scatter(20)
    Umatplotlib.hist2(10000)
