# coding=utf-8

from datetime import datetime


def is_leap_year(year):
    is_leep = False
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        is_leap = True
    return is_leep


def main():
    date_str = input("请输入日期(yyyy/mm/dd)")
    input_date = datetime.strptime(date_str, "%Y/%m/%d")
    print(input_date)
    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    days = sum(days_in_month_tup[:input_date.month-1])
    days += input_date.day

    if(input_date.month > 2 and is_leap_year(input_date.year)):
        days += 1
    print(str.format("这是第{}天", days))


if __name__ == '__main__':
    main()
