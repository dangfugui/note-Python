#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
pip install -i https://pypi.douban.com/simple/ beautifulsoup4 lxml
pip install --user beautifulsoup4 lxml
@author: duang
'''
import os
from bs4 import BeautifulSoup
import logging as log
import spider_tool

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s %(name)s %(levelname)s %(message)s",
                datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                )

# root_url = "https://www.6234pu.com/"
# root_url = "https://www.3567na.com/"
# root_url = "https://www.3678qi.com/"
# root_url = "https://www.6678nv.com/"
root_url = "https://www.3345ou.com"
# work_path = "/e/temp/" + (time.strftime("%Y-%m-%d", time.localtime())) + '/'
work_path = "/srv/dev-disk-by-label-cache/_download/home/"

aria2_list = []


def parserLi(li):
    name = li.find_all("a")[1].text
    infoUrl = root_url + li.find_all("a")[1]['href']
    imageUrl = li.find_all("a")[0]['data-original']
    time = li.find("span", {"class": "note"}).text
    log.info("parser li: name:[%s] image:{%s} infoUrl:{%s}", name, imageUrl, infoUrl)
    # 进入详情页
    soup = BeautifulSoup(spider_tool.get_page(infoUrl), 'lxml')
    type = soup.find("div", {"id": "detail-box"}).find_all('dd')[0].a.text
    day_path = work_path + time + "/"
    if not os.path.exists(day_path):
        os.makedirs(day_path)
    # 下载图片
    imagepath = day_path + type + "___" + name + imageUrl[-4:]
    if not os.path.exists(imagepath):
        spider_tool.down_file(imageUrl, imagepath)
    # 进入下载页面
    downUrl = root_url + soup.find_all("div", {"class": "ui-box border-gray clearfix"})[1].find_all("a")[1].attrs[
        "href"]
    downSoup = BeautifulSoup(spider_tool.get_page(downUrl), 'lxml')
    videoUrl = downSoup.find("div", {"class": "download"}).a.attrs["href"]
    log.info("start down:type:[%s] name:[%s] video:{%s} path:{%s}", type, name, videoUrl,
             day_path + type + "___" + name + videoUrl[-4:])
    # t = spider_tool.download_aria2(videoUrl, type + "___" + name + videoUrl[-4:], day_path)
    aria2_list.append({"url": videoUrl, "name": type + "___" + name + videoUrl[-4:], "path": day_path})
    log.info("end down:type:[%s] name:[%s] video:{%s} path:{%s}", type, name, videoUrl,
             day_path + type + "___" + name + videoUrl[-4:])
    # time.sleep(10) # sleep 10秒


def start():
    isExists = os.path.exists(work_path)
    if not isExists:
        os.makedirs(work_path)
    soup = BeautifulSoup(spider_tool.get_page(root_url), 'lxml')
    ul = soup.find_all('ul', {'class': 'clearfix'})[0]
    for li in ul.find_all('li'):
        try:
            parserLi(li)
        except Exception as err:
            log.error(err)
    for dict in aria2_list:
        spider_tool.download_aria2(dict['url'], dict['name'], dict['path'])


if __name__ == '__main__':
    start()
