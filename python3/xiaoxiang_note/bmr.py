
def bmr():
    is_exit = "n"
    while is_exit == "n":
        gender = input("性别")
        weight = eval(input("体重（kg:）"))
        height = eval(input("身高（cm）:"))
        age = eval(input("年龄："))
        if gender == "男":
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == "女":
            bmr = (9.6 * weight) + (1.8 * height) + 655
        else:
            print("不支持性别", gender)
        print("BMR:{}大卡".format(bmr))
        is_exit = input("是否退出程序(y/n)")


def bmr_v2():
    is_exit = "n"
    print("请依次输入一下信息，用空格隔开")
    while is_exit == "n":
        input_arr = input("性别 体重(kg) 身高(cm) 年龄\n").split(" ")
        gender = input_arr[0]
        weight = eval(input_arr[1])
        height = eval(input_arr[2])
        age = eval(input_arr[3])
        if gender == "男":
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == "女":
            bmr = (9.6 * weight) + (1.8 * height) + 655
        else:
            print("不支持性别", gender)
        print("BMR:{}大卡".format(bmr))
        is_exit = input("是否退出程序(y/n)")


if __name__ == '__main__':
    bmr_v2()
