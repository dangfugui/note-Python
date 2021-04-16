#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time, sys
import json
import ConfigParser
import logging as log

reload(sys)
sys.setdefaultencoding("utf-8")
print sys.getdefaultencoding()
log.basicConfig(filename='jd.log', level=log.INFO,
                format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
is_debug = True
config = ConfigParser.ConfigParser()
config.read("config.ini")
goods = config.options("GOODS")


def open_page(browser):
    # http://npm.taobao.org/mirrors/chromedriver/90.0.4430.24/
    browser.get("https://paipai.m.jd.com/ppdbd/pages/index/index?entryid=p0020002sszd190326&scene=null")
    time.sleep(5)
    list = browser.find_elements_by_class_name("item-view")
    for item in list:
        values = item.text.encode("utf-8").split("\n")
        log.info("%s_|_%s_|_%s_|_%s" % (values[1], values[3], values[6], values[8]))
        if values[1] in goods:
            item.click()
    time.sleep(11111)


def login():
    # http://npm.taobao.org/mirrors/chromedriver/90.0.4430.24/
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('mobileEmulation', {'deviceName': 'Galaxy S5'})
    if not is_debug:
        options.add_argument("headless")
        options.add_argument("disable-gpu")
    browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe",
                               chrome_options=options)
    browser.set_window_size(500, 900)
    browser.get("https://plogin.m.jd.com/login/login")
    # for i in cookie_str.split(";"):
    #     cookie={"name" : i.split("=")[0], "value" : i.split("=")[1], 'Domain': 'paipai.m.jd.com'}
    #     browser.add_cookie(cookie)
    cookies = json.loads(config.get("JD", "cookie_json"))
    browser.delete_all_cookies()
    for c in cookies:
        browser.add_cookie(c)
    return browser


if __name__ == '__main__':
    print("开始")
    browser = login()
    for i in range(1):
        open_page(browser)
    browser.quit()


def exitfunc():
    log.info("exitfunc start")
    with open("config.ini", "w+") as f: config.write(f)
