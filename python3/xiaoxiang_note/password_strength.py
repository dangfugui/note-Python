# coding=utf-8


def check_number_exist(password_str):
    has_number = False
    for s in password_str:
        if s.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password_str):
    has_letter = False
    for s in password_str:
        if s.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    password_str = input("请输入密码")
    level = 0
    if len(password_str) > 8:
        level += 1
    if check_number_exist(password_str):
        level += 1
    if check_letter_exist(password_str):
        level += 1
    print("密码强度：", level)
    f = open("password.txt", "a")   # a 追加
    f.write(password_str+"\n")
    f.close()


def read_file():
    f = open("password.txt", "r")
    for line in f.readlines():
        print(line)
    f.close()

    
if __name__ == '__main__':
    # main()
    read_file()
