#!/usr/bin/python
# -*- coding:utf-8 -*-

USD_VS_RMB = 6.77


def converter_v1():
    rmb_str = input('输入人民币金额:')
    usd_value = eval(rmb_str) / USD_VS_RMB
    print('美元（USD）金额为：', usd_value)
#####################################################################


def converter_v2():
    currency_str = input('请输入带单位的金额:')
    if currency_str[-3:] == 'CNY':
        rmb_str = currency_str[:-3]
        usd_value = eval(rmb_str) / USD_VS_RMB
        print('美元（USD）金额为：', usd_value)
    elif currency_str[-3:] == 'USD':
        usd_value = eval(currency_str[:-3])
        print("人民币（CNY）金额为：", usd_value * USD_VS_RMB)
    elif currency_str == 'quit':
        exit()
    else:
        print("不支持币种")
    return
#####################################################################


def converter_v3():
    i = 0;
    while True:
        i = i + 1
        print(i, "******************************************")
        converter_v2()
#####################################################################


def convert_currency(in_mony, exchange_rate):
    return in_mony * exchange_rate


def converter_v4():
    """
        汇率兑换
    :return:金额
    """
    currency_str = input('请输入带单位的金额:')
    unit = currency_str[-3:]
    exchange_rate = 0
    if unit == 'CNY':
        exchange_rate = 1/USD_VS_RMB
    elif unit == 'USD':
        exchange_rate = USD_VS_RMB
    else:
        exchange_rate = -1

    if exchange_rate != -1:
        convert_currency2 = lambda x: x * exchange_rate
        in_mony = eval(currency_str[:-3])
        # out_money = convert_currency(in_mony, exchange_rate)
        out_money = convert_currency2(in_mony)
        print(out_money)


if __name__ == '__main__':
    converter_v4()
