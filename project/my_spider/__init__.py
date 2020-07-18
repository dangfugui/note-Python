#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
pip install -i https://pypi.douban.com/simple/ beautifulsoup4 lxml
pip install --user beautifulsoup4 lxml
@author: duang
'''
import logging as log
import download_tool

log.basicConfig(level=log.INFO,
                format="%(asctime)s %(name)s %(levelname)s %(message)s",
                datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                )

# if __name__ == '__main__':
#     start()
    # downFile('https://pppp.642p.com/image/202004/xj3l9sLu.jpg', work_path + 'test.jpg')
