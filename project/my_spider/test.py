import asyncio
import time
import threading
import os
import gevent

async def sleep(x):
    print('函数的线程ID：', threading.get_ident())
    print('协程目标：', gevent.getcurrent(), x)
    await asyncio.sleep(x)      # 注意这里不是time.sleep()，若使用time.sleep()将会导致线程阻塞
    return 'Hello'

if __name__ == '__main__':
    t1 = time.time()
    print('主进程PID:',os.getpid())
    print('主程序线程ID：', threading.get_ident())
    tasks = []
    for x in range(0, 5):
        tasks.append(asyncio.ensure_future(sleep(2)))

    # tasks = [asyncio.ensure_future(sleep(2)) for x in range(0, 5)]  # 获取任务列表
    loop = asyncio.get_event_loop()  # 得到一个标准的事件循环
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)

    t2 = time.time()
    print('使用异步方法，总共耗时 %s' % (t2 - t1))
