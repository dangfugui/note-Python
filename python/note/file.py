#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月27日
@author: duang
'''

def text_create(name, msg):
    desktop_path = 'd:/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
#text_create('hello','hello world') # 

def text_read(path):
    with open(path,'r') as text:
        words = [raw_word.strip('!@#$%^&*()_+<>?:.').lower() for raw_word in text.read().split()]
        words_index = set(words)
        counts_dict = {index:words.count(index) for index in words_index}
    for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
        print('{} -- {} times'.format(word,counts_dict[word]))
        #words=text.read().split()
        #for word in words:
        #   print('{}-{} tims'.format(word,words.count(word)))
#text_read('d:/Files/my code/python/file/Walden.txt')
import sys,os
#获取脚本文件的当前路径
def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
#打印结果
path=cur_file_dir()


