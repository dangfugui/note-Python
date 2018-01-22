# coding=utf-8
import random
import matplotlib.pylab as plt


class RandomTool:


    def __init__(self):
        pass

    def start(self, size, count):
        result_list = [0] * size
        for i in range(count):
            random_int = random.randint(1, size)
            result_list[random_int - 1] += 1
        return result_list

    @staticmethod
    def roll(roll_size, count):
        roll_list = list(range(roll_size * 1, roll_size * 6 + 1))
        roll_dict = dict(zip(roll_list, [0] * len(roll_list)))
        for i in range(count):
            roll_sum = 0
            for index in range(roll_size):
                roll_sum += random.randint(1, 6)
            roll_dict[roll_sum] += 1
        return roll_dict

    @staticmethod
    def print_list(alist):
        for i, x in enumerate(alist):
            print(str.format("点数{} 的次数：{} 频率为：{}", i+1, x, x/sum(alist)))

    @staticmethod
    def print_dict(adict):
        totle_times = 0
        for k, v in adict.items():
            totle_times += v
        for k, v in adict.items():
            print(str.format("点数{} 的次数：{} 频率为：{}", k, v, v / totle_times))

    @staticmethod
    def show(count):
        roll1_list = []
        roll2_list = []
        for i in range(count):
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            roll1_list.append(roll1)
            roll2_list.append(roll2)
        x = range(1, count + 1)
        plt.scatter(x, roll1_list,  alpha=0.5, c="red")
        plt.scatter(x, roll2_list,  alpha=0.5, c="green")
        plt.show()


if __name__ == '__main__':
    randomTool = RandomTool()
    # res = randomTool.start(6, 10000)
    # randomTool.print_list(res)
    # res = randomTool.roll(2, 100)
    # randomTool.print_dict(res)
    RandomTool.show(100)
