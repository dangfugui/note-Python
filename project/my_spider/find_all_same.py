#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@author: duang
'''
import sys, os, csv
import logging as log

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s %(name)s %(levelname)s %(message)s",
                datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                )
# find_dir_list = ['D:\srv\dev-disk-by-label-share\_download']
find_dir_list = ['/srv/dev-disk-by-label-File/yaoyao/_download']

class Myfile:
    name = ''
    path = ''
    size = 0
    label = 'file'

    def __init__(self, path, size, name=''):
        self.path = path
        self.size = size
        self.name = name

    def __str__(self):
        return "myFile size: %10d \t name: %s \t path: %s " % (self.size, self.name, self.path)


def list_all_file(file_list, dir):
    for home, dirs, files in os.walk(dir):
        for filename in files:
            path = os.path.join(home, filename)
            size = 0
            try:
                size = os.path.getsize(path)
            except:
                log.warning("get size :%s", path)
            file = Myfile(path, size, filename)
            file_list.append(file)
            log.info('find_file:%s', file)


def tocsv(file, header, data):
    with open(file, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)


def addlabel(file_list):
    file_list.sort(key=lambda f: (f.size, -len(f.name)))
    for i in range(1, len(file_list)):
        file = file_list[i]
        if file.size == file_list[i - 1].size: file.label = file.label + ('|size')
        if file.name == file_list[i - 1].name: file.label = file.label + ('|name')
        elif file.name[8:-12] in file_list[i - 1].name: file.label = file.label + ('|same')


def find(dir_list=find_dir_list):
    if len(sys.argv) > 2:  # 如果有传参数 第一个参数是root url
        for i in range(2, -len(sys.argv)):
            find_dir_list.append(sys.argv[i])
    file_list = []
    for dir in dir_list:
        list_all_file(file_list, dir)
    addlabel(file_list)
    data = []
    for file in file_list:
        data.append([file.label, file.size, file.name, file.path])
    tocsv('all_find_file.csv', ['label', 'size', 'name', 'path'], data)


def remove():
    file = sys.argv[2]
    label = sys.argv[3]
    with open(file, encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        header = next(reader)
        log.info("csv_header:%s", header)
        for row in reader:
            if label in row[0]:
                if os.path.exists(row[3]):
                    log.info("remove_file:%s", row)
                    os.remove(row[3])
                else:
                    log.info("not_exists_file:%s", row)


if __name__ == "__main__":
    log.info("arg:%s", sys.argv)
    fun_name = sys.argv[1]
    if fun_name == 'find':
        find(find_dir_list)
    elif fun_name == 'remove':
        remove()
    log.info('end')
