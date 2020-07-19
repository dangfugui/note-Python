#! -coding:utf8 -*-
from pyaria2 import Aria2RPC
import sys
import os

# ['/Users/csx/GitProject/snowmusic/pyaria2-jsonrpc/hook.py', 'e3f97be6d4490a5a', '1', './temp/aa.mp3']
Argv = sys.argv

# 这里自己编写任意的回调函数，可以进行更新数据库等操作
def Hook(Argv):
    print(Argv)


jsonrpc = Aria2RPC(url="http://192.168.11.11:6800/rpc")
set_dir = os.path.dirname(__file__)
work_path = "/srv/dev-disk-by-label-cache/_download/"
file_name = 'test_2bFwkbFt.mp4'
options = {"dir": work_path, "out": file_name, }
link = "https://d2.xia12345.com/down/109/2020/04/2bFwkbFt.mp4"
res = jsonrpc.addUri([link], options = options)
print(res)

resp = jsonrpc.addUri('https://music.snowmusic.cc/radio/13714_1507261169_4.mp3', options={"out": "aa.mp3"})
