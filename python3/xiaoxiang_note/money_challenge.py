
import math

saving = 0
def main():
    money_per_week = 10
    week = 1
    increase_money = 10
    total_week = 52
    global saving   # 这个函数的saving是对全局的saving操作
    money_list = []
    while week <= total_week:
        saving += money_per_week
        money_list.append(money_per_week)
        print(str.format("第{}周 存入{}元 账户累计{}元", week, money_per_week, saving))
        money_per_week += increase_money
        week += 1

    for i in money_list:
        print(i)
    print("sum:", math.fsum(money_list))


if __name__ == '__main__':
    main()
