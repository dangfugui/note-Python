
"""
    绘制五角星
"""

import turtle


class Pentagram(object):

    @staticmethod
    def note():
        # 画笔向前移动distance距离
        turtle.forward(300)
        # 画笔向后移动
        turtle.backward(100)
        # 向右旋转144度
        turtle.right(144)
        # 抬起笔
        turtle.penup()
        turtle.forward(100)
        # 落下笔
        turtle.pendown()
        turtle.pensize(5)
        turtle.pencolor('red')
        turtle.forward(100)
        # 点击关闭图形窗口
        turtle.exitonclick()

    @staticmethod
    def v1():
        for i in range(5):
            # 画笔向前移动distance距离
            turtle.forward(300)
            # 画笔向后移动
            # turtle.backward(10)
            # 向右旋转144度
            turtle.right(144)
            # 点击关闭图形窗口
        turtle.exitonclick()
#########################################################

    @staticmethod
    def pentagram(size):
        for i in range(5):
            turtle.forward(size)
            turtle.right(144)
        return turtle

    @staticmethod
    def v2(size=100, count=1, step=0):
        istep = 0
        for i in range(count):
            Pentagram.pentagram(size + istep)
            istep += step


if __name__ == '__main__':
    pen = Pentagram()
    pen.note()
    # pen.v2(100, 5, 50)

