# -*- coding: utf8 -*-
__author__ = 'liuyuanjun'

import socket
import threading, time

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(1)
# s.connect(('172.25.47.214', 61888))
# s.bind(('127.0.0.1', 58722))
# s.listen(1)         #开始TCP监听
# while 1:
#     conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
#     print'Connected by',addr    #输出客户端的IP地址
#     while 1:
#         conn.sendall('hello')
#         data=conn.recv(1024)    #把接收的数据实例化
#         print data
#         conn.close()     #关闭连接
def conn2(i):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(20)
    s.connect(('172.25.47.214', 61888))
    print '第'+str(i)+'个线程。。。'+str(s.getsockname())
    time.sleep(1000)

threads = []
for i in range(10000):
    threads.append(threading.Thread(target=conn2,args=(i,)))

for t in threads:
    t.setDaemon(True)
    t.start()

t.join()
print 'ok'