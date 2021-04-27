#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time, sys
import json
import ConfigParser
import logging as log

reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()
log.basicConfig(filename='sendCode.log', level=log.INFO,
                format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
is_debug = True


def sendBaidu(browser, phone):
    browser.get(
        "https://passport.baidu.com/v2/?reg&tt=1619331453568&overseas=&gid=44E6565-1760-4251-A0D0-98D6B316FFD8&tpl=pp&u=https%3A%2F%2Fpassport.baidu.com%2F")
    browser.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("c_n1jmdbhq")
    browser.find_element_by_id("TANGRAM__PSP_4__phone").send_keys(phone)
    browser.find_element_by_id("TANGRAM__PSP_4__password").send_keys("cn1jmdbhq")
    time.sleep(2)
    browser.find_element_by_id("TANGRAM__PSP_4__verifyCodeSend").click()


def sendYidong(browser, phone):
    browser.get(
        "https://login.10086.cn/login.html?channelID=12034&backUrl=http%3A%2F%2Fwww.10086.cn%2Findex%2Fbj%2Findex_100_100.html%3FWT.mc_id%3Dj4cjLiavhrFcg0AFIYX5_pBXyfgThb1krbzlPjwj71619332385.465wm0x123d123o216t22xm0w")
    time.sleep(2)
    browser.find_element_by_id("p_name").send_keys(phone)
    browser.find_element_by_id("p_pwd").send_keys('444444')
    time.sleep(2)
    browser.find_element_by_id("getSMSPwd").click()


def sendWeibo(browser, phone):
    browser.get("https://weibo.com/signup/signup.php")
    time.sleep(2)
    browser.find_element_by_name("username").send_keys(phone)
    browser.find_element_by_name("passwd").send_keys('cn1jmdbhq')
    time.sleep(2)
    browser.find_element_by_class_name("W_btn_e").click()


def sendYijia(browser, phone):
    browser.get("https://id.oneplus.com/index.html?&callback=https%3A%2F%2Fwww.oneplus.com%2Fcn&language=zh-CN")
    time.sleep(2)
    browser.find_elements_by_xpath("//input")[0].send_keys(phone)
    time.sleep(2)
    browser.find_element_by_class_name("input_code").click()


def sendFeisu(browser, phone):
    browser.get("https://www.feishu.cn/create/?redirect_uri=https%3A%2F%2Fwww.feishu.cn%2F&app_id=11")
    time.sleep(2)
    browser.find_element_by_id("register_phone").send_keys(phone)
    browser.find_element_by_class_name("pp-base-button").click()
    time.sleep(2)
    browser.find_element_by_class_name("operation-switch").click()


def sendCode(phone,sleeptime):
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('mobileEmulation', {'deviceName': 'Galaxy S5'})
    if not is_debug:
        options.add_argument("headless")
        options.add_argument("disable-gpu")
    browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe",
                               chrome_options=options)
    # browser.set_window_size(500, 900)
    try:
        sendBaidu(browser,phone)
    except:
        pass
    time.sleep(sleeptime)
    try:
        sendYidong(browser,phone)
    except:
        pass
    time.sleep(sleeptime)
    try:
        sendWeibo(browser,phone)
    except:
        pass
    time.sleep(sleeptime)
    try:
        sendYijia(browser, phone)
    except:
        pass
    time.sleep(sleeptime)
    try:
        sendFeisu(browser, phone)
    except:
        pass
    time.sleep(sleeptime)
    print "end"


if __name__ == '__main__':
    print("开始")
    sendCode("16622075108",10)
