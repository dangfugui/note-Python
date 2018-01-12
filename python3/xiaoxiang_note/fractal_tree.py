

import turtle

# class FractalTree():


def draw_branch(branch_length, step):
    if branch_length < 5:
        return
    # 绘制树枝
    turtle.forward(branch_length)
    # 绘制右侧树枝
    turtle.right(20)
    draw_branch(branch_length - step, step)
    # 绘制右侧树枝
    turtle.left(40)
    draw_branch(branch_length - step, step)
    # 返回之前的树枝
    turtle.right(20)
    turtle.backward(branch_length)


def draw_tree(length=100, step=15):
    turtle  # type: turtle
    turtle.speed(10000000)
    turtle.left(90)
    turtle.penup()
    turtle.backward(length)
    turtle.pendown()
    turtle.color("brown")
    draw_branch(length, step)
    turtle.exitonclick()


if __name__ == '__main__':
    draw_tree(90, 10)
