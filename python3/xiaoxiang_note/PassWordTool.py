# coding=utf-8


class PasswordTool:

    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def check_number_exist(self):
        has_number = False
        for s in self.password:
            if s.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        has_letter = False
        for s in self.password:
            if s.isalpha():
                has_letter = True
                break
        return has_letter

    def process_password(self):
        if len(self.password) > 8:
            self.strength_level += 1
        if self.check_number_exist():
            self.strength_level += 1
        if self.check_letter_exist():
            self.strength_level += 1
        print("密码强度：", self.strength_level)
        return self.strength_level


if __name__ == '__main__':
    password = input("请输入密码")
    passwordTool = PasswordTool(password)
    level = passwordTool.process_password()
    print(level)
