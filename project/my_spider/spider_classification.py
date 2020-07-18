#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
pip install -i https://pypi.douban.com/simple/ beautifulsoup4 lxml
pip install --user beautifulsoup4 lxml
@author: duang
'''
import os
import time
import urllib
from bs4 import BeautifulSoup
from lxml import etree
import logging as log
import download_tool

log.basicConfig(level=log.INFO,
                format="%(asctime)s %(name)s %(levelname)s %(message)s",
                datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                )

root_url = "https://www.6234pu.com/"
type_path = "/vod/html10/"
# root_url = "https://www.3567na.com/"
# work_path = "/e/temp/" + (time.strftime("%Y-%m-%d", time.localtime())) + '/'
work_path = "/e/spider_classification/"
thread_count=5

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}


def getPage(url):
    '''
    下载页面源码
    :param url: url地址
    :return: html 源码
    '''
    # pretend to be a chrome 47 browser on a windows 10 machine
    req = urllib.request.Request(url, headers=headers)
    # open the url
    x = urllib.request.urlopen(req)
    # get the source code
    sourceCode = x.read()
    return sourceCode


def downFile(url, path):
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    pic = response.read()
    with open(path, 'wb') as f:
        f.write(pic)


def parserLi(li):
    name = li.find_all("a")[1].text
    infoUrl = root_url + li.find_all("a")[1]['href']
    imageUrl = li.find_all("a")[0]['data-original']
    time = li.find("span", {"class": "note"}).text
    log.info("parser li: name:[%s] image:{%s} infoUrl:{%s}", name, imageUrl, infoUrl)
    # 进入详情页
    soup = BeautifulSoup(getPage(infoUrl), 'lxml')
    type = soup.find("div", {"id": "detail-box"}).find_all('dd')[0].a.text
    day_path = work_path + time + "/"
    isExists = os.path.exists(day_path)
    if not isExists:
        os.makedirs(day_path)
    downFile(imageUrl, day_path + type + "___" + name + imageUrl[-4:])
    downUrl = root_url + soup.find_all("div", {"class": "ui-box border-gray clearfix"})[1].find_all("a")[1].attrs[
        "href"]
    # 进入下载页
    downSoup = BeautifulSoup(getPage(downUrl), 'lxml')
    videoUrl = downSoup.find("div", {"class": "download"}).a.attrs["href"]
    log.info("start down:type:[%s] name:[%s] video:{%s} path:{%s}", type, name, videoUrl,
             day_path + type + "___" + name + videoUrl[-4:])
    # downFile(videoUrl,day_path + type + "___" + name + videoUrl[-4:])
    t = download_tool.download(videoUrl, day_path + type + "___" + name + videoUrl[-4:], thread_count)
    t.join()


def start():
    isExists = os.path.exists(work_path)
    if not isExists:
        os.makedirs(work_path)
    soup = BeautifulSoup(getPage(root_url+type_path), 'lxml')
    for li in soup.find_all('ul', {'class': 'clearfix'})[0]:
        try:
            parserLi(li)
        except Exception as err:
            log.error(err)


if __name__ == '__main__':
    start()
