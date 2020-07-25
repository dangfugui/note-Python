#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
pip install -i https://pypi.douban.com/simple/ beautifulsoup4 lxml
pip install --user beautifulsoup4 lxml
@author: duang
'''
import os, sys, time, threading
from bs4 import BeautifulSoup
import logging as log
import spider_tool
import gevent, time
from gevent import monkey

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s %(name)s %(levelname)s %(message)s",
                datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                )

# root_url = "https://www.6234pu.com/"
# root_url = "https://www.3567na.com/"
# root_url = "https://www.3678qi.com/"
# root_url = "https://www.6678nv.com/"
# root_url = "https://www.3345ou.com"
# root_url = "https://www.6234nv.com/"
root_url = "https://www.6234ca.com/"

# https://www.6234nv.com/vod/html16/index_2.html
work_path = "/srv/dev-disk-by-label-share/_download/class/"
check_path = "/srv/dev-disk-by-label-File/yaoyao/_download/class/"
check_du_file = "/srv/dev-disk-by-label-share/_python/du_all.txt"
is_prod = True

type_list = [
    {'href': '/', 'type': '#首页'},  ## 一级页
    {'href': '/vod/html1/', 'type': '#国产精品'},  ## 一级页
    {'href': '/vod/html2/', 'type': '自拍偷拍'},
    {'href': '/vod/html3/', 'type': '夫妻同房'},
    {'href': '/vod/html4/', 'type': '开放90后'},
    {'href': '/vod/html5/', 'type': '换妻游戏'},
    {'href': '/vod/html6/', 'type': '网红主播'},
    {'href': '/vod/html7/', 'type': '手机小视频'},
    {'href': '/vod/html8/', 'type': '经典三级'},
    {'href': '/vod/html9/', 'type': '#亚洲无码'},  ## 一级页
    # {'href': '/vod/html10/', 'type': '无码中字'},
    # {'href': '/vod/html9/html22/', 'type': 'S级女优'},
    # {'href': '/vod/html34/', 'type': 'SM系列'},
    # {'href': '/vod/html11/', 'type': '熟女人妻'},
    # {'href': '/vod/html12/', 'type': '美颜巨乳'},
    # {'href': '/vod/html13/', 'type': '颜射吃精'},
    # {'href': '/vod/html14/', 'type': '丝袜制服'},
    # {'href': '/vod/html15/', 'type': '高清无码'},
    {'href': '/vod/html16/', 'type': '中文有码'},
    {'href': '/vod/html17/', 'type': '#著名女优'},  ## 一级页
    # {'href':'/vod/html18/', 'type':'宇都宮紫苑'},
    # {'href':'/vod/html19/', 'type':'天海翼'},
    # {'href':'/vod/html20/', 'type':'水菜麗'},
    # {'href':'/vod/html21/', 'type':'泷泽萝拉'},
    # {'href':'/vod/html23/', 'type':'波多野结衣'},
    # {'href':'/vod/html24/', 'type':'吉泽明步'},
    # {'href':'/vod/html25/', 'type':'苍井空'},
    # {'href':'/vod/html35/', 'type':'樱井莉亚'},
    # {'href':'/vod/html36/', 'type':'小川阿佐美'},
    # {'href':'/vod/html37/', 'type':'松岛枫'},
    # {'href':'/vod/html38/', 'type':'冬月枫'},
    # {'href':'/vod/html39/', 'type':'三上悠亚'},
    # {'href':'/vod/html40/', 'type':'桥本凉'},
    # {'href':'/vod/html41/', 'type':'北野望'},
    # {'href':'/vod/html42/', 'type':'大桥未久'},
    {'href': '/vod/html26/', 'type': '动漫卡通'},
    {'href': '/vod/html27/', 'type': '欧美系列'}
]


def exists_check(url, filename, dir_path):
    # 读取文件里面每一行
    with open(check_du_file, encoding='utf-8') as f:
        for line in f.readlines():
            if line.find(filename) != -1: 
                log.info("check_du exists  url:[%s] line:[%s]",url, line)
                return True

    flie_path = dir_path + "/" + filename
    check_file = flie_path.replace(work_path, check_path)
    if os.path.exists(check_file):
        log.info("check_path exists path:[%s] url:[%s]", check_file, url)
        return True
    return False


def parserLi(li, index=1):
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
    spider_tool.down_file(imageUrl, imagepath)
    # 进入下载页面
    downUrl = root_url + soup.find_all("div", {"class": "ui-box border-gray clearfix"})[1].find_all("a")[1].attrs[
        "href"]
    downSoup = BeautifulSoup(spider_tool.get_page(downUrl), 'lxml')
    videoUrl = downSoup.find("div", {"class": "download"}).a.attrs["href"]
    log.info("li end:type:[%s] name:[%s] video:{%s} path:{%s}", type, name, videoUrl,
             day_path + type + "___" + name + videoUrl[-4:])
    # t = spider_tool.download_aria2(videoUrl, type + "___" + name + videoUrl[-4:], day_path)
    return {"url": videoUrl, "name": type + "___" + name + videoUrl[-4:], "path": day_path}
    # time.sleep(10) # sleep 10秒


def start_spider(url=root_url, info=""):
    t1 = time.time()
    log.info("start spider: %s info:%s 线程ID:%s", url, info, threading.get_ident())
    soup = BeautifulSoup(spider_tool.get_page(url), 'lxml')
    aria2_list = []
    monkey.patch_all()  # 将程序中所有IO操作做上标记使程序非阻塞状态
    g_list = []
    ul_list = soup.find_all('ul', {'class': 'clearfix'})
    for ul_index in range(0, len(ul_list) - 1):
        for li in ul_list[ul_index].find_all('li'):
            try:
                # parserLi(li)
                g_list.append(gevent.spawn(parserLi, li))
            except Exception as err:
                log.error(err)
    gevent.joinall(g_list)
    time.sleep(5)
    for i, g in enumerate(g_list):
        dict = g.value
        log.info("spider_tool.download_aria2(%s,%s,%s)", dict['url'], dict['name'], dict['path'])
        if not exists_check(dict['url'], dict['name'], dict['path']) and is_prod:
            spider_tool.download_aria2(dict['url'], dict['name'], dict['path'])
    t2 = time.time()
    log.info("end spider:总共耗时:%s url:%s info:%s 线程ID:%s", (t2 - t1), url, info, threading.get_ident())


if __name__ == '__main__':
    monkey.patch_all()
    if len(sys.argv) > 1:  # 如果有传参数 第一个参数是root url
        root_url = sys.argv[1]
    for item in type_list:
        try:
            start_spider(root_url + item['href'], item['type'])
            # pass
        except Exception as err:
            log.error(err)
    for page in range(5, 15):  ## 左开右闭
        for item in type_list:
            if "#" not in item['type']:
                try:
                    start_spider(root_url + item['href'] + "/index_" + str(page) + ".html", item['type'])
                except Exception as err:
                    log.error(err)
    log.info("python end")
