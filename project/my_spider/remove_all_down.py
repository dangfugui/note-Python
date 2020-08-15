#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@author: duang
'''
import sys, os
import logging as log

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s %(name)s %(levelname)s %(message)s",
                datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                )
down_path = "/srv/dev-disk-by-label-share/_download"
check_du_file = "/srv/dev-disk-by-label-share/_python/du_all.txt"
all_file_dict = {}

def exists_check(filename):
    # 读取文件里面每一行
    if len(all_file_dict) == 0: 
        with open(check_du_file, encoding='utf-8') as f:
            for line in f.readlines():
                key = os.path.split(line)[-1].strip()
                all_file_dict[key] = line.strip()
                log.info("add_dict: %s = %s",key,line.strip())
        print(all_file_dict.keys)
    key = os.path.split(filename)[-1].strip()
    # log.info("dict_find:[%s]  = %s",key,all_file_dict.get(key))
    if key in all_file_dict:
        log.info("dict_find:[%s]  = %s",key,all_file_dict.get(key))
        return True
    else:
        log.info("dict_not_find:%s",key)
        return False
    

def get_filelist(dir):
    for home, dirs, files in os.walk(dir):
        # print("#######dir list#######")
        # for dir in dirs:
        #     print(dir)
        for filename in files:
            # print(filename)
            if '.mp4' in filename:
                # fullname = os.path.join(home, filename)
                aria_name = filename + '.aria2'
                if os.path.exists(os.path.join(home, aria_name)):
                     log.info("aria2_exists:[%s]", filename)
                     continue
                elif exists_check(filename):
                    os.remove(os.path.join(home, filename))
                    log.info("remove_mp4:[%s]", filename)
               

if __name__ == "__main__":
    log.info("path" + down_path)
    get_filelist(down_path)
    log.info('end')
