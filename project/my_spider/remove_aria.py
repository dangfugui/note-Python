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


def get_filelist(dir):
    count = 1
    for home, dirs, files in os.walk(dir):
        # print("#######dir list#######")
        # for dir in dirs:
        #     print(dir)

        for filename in files:
            # print(filename)
            if '.aria2' in filename:
                # fullname = os.path.join(home, filename)
                mp4name = filename[:-6]
                imagejpg = filename[:-10] + '.jpg'
                imagegif = filename[:-10] + '.gif'
                log.info("find_%d aria:[%s]", count, filename)
                count = count + 1
                if os.path.exists(os.path.join(home, mp4name)):
                    # os.remove(os.path.join(home, mp4name))
                    log.info("remove_mp4:[%s]", mp4name)
                if os.path.exists(os.path.join(home, imagejpg)):
                    os.remove(os.path.join(home, imagejpg))
                log.info("remove_imagejpg:[%s]", imagejpg)
                if os.path.exists(os.path.join(home, imagegif)):
                    os.remove(os.path.join(home, imagegif))
                log.info("remove_imagegif:[%s]", imagegif)
                if os.path.exists(os.path.join(home, filename)):
                    # os.remove(os.path.join(home, filename))
                    log.info("remove_aria2:[%s]", filename)


if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(sys.argv[0]) + os.path.sep + ".")
    log.info("path" + path)
    get_filelist(path)
    log.info('end')
