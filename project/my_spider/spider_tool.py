#! -coding:utf8 -*-
from pyaria2 import Aria2RPC
import logging as log
import urllib, requests
import os, time, threading

log.basicConfig(level=log.DEBUG,
                format="%(asctime)s %(name)s %(levelname)s %(message)s",
                datefmt='%Y-%m-%d  %H:%M:%S %a'  # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
                )
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
}

conf_timeout = 60 * 10

def get_page(url):
    log.info("get_page:[%s]", url)
    req = urllib.request.Request(url, headers=headers)
    x = urllib.request.urlopen(req, timeout=conf_timeout)
    source_code = x.read()
    return source_code


def down_file(url, path):
    if os.path.exists(path):
        log.info("down_exists:[%s] path:[%s]", url, path)
        return
    log.info("down_file:[%s] path:[%s]", url, path)
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req,timeout=conf_timeout)
    chunk = 16 * 1024
    with open(path, 'wb') as f:
        while True:
            chunk = response.read(chunk)
            if not chunk:
                break
            f.write(chunk)


def download_aria2(url, filename, work_path="/srv/dev-disk-by-label-cache/_download/"):
    if os.path.exists(work_path + "/" + filename):
        log.info("aria2 exists path:[%s] url:[%s] filename:[%s]", work_path, url, filename)
        return
    if not os.path.exists(work_path):
        log.warning("makedirs:[%s]", work_path)
        os.makedirs(work_path, mode=0o777, exist_ok=False)
    log.info("aria2down path:[%s] url:[%s] filename:[%s]", work_path, url, filename)
    jsonrpc = Aria2RPC(url="http://192.168.0.11:6800/rpc")
    options = {"dir": work_path, "out": filename, }
    hook_id = jsonrpc.addUri([url], options=options)
    log.info("aria2down path:[%s] url:[%s] filename:[%s] hookid:[%s]", work_path, url, filename, hook_id)


def download_multithread(url, filename, thread_count=5, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3559.6 Safari/537.36'}):
    log.info("down_file:[%s] path:[%s]", url, filename)
    t = DownloadWorkerThread(url, filename, headers=headers, thread_count=thread_count)
    t.start()
    return t


# 处理单个下载线程
class DownloadWorkerThread(threading.Thread):
    thread_count = 10
    file_lock = threading.Lock()
    fileinfo_lock = threading.Lock()

    def __init__(self, url, filename, headers={}, thread_count=3):
        threading.Thread.__init__(self)
        self.filename = filename
        self.url = url
        self.fileinfo_name = filename + ".tmp"
        self.headers = headers
        self.thread_count = thread_count
        if os.path.exists(self.fileinfo_name):
            os.remove(self.fileinfo_name)
            os.remove(self.filename)

    def run(self):
        if os.path.exists(self.filename):
            return
        self.range_manager = self.read_range_file()
        log.info(u"Begin Downloading \nurl= " + self.url + "\nfilename = " + self.filename)
        if self.url.strip() == "":
            return
        tlst = []
        for i in range(self.thread_count):
            t = threading.Thread(target=self.RangeWorker, args=(self,))
            log.info(u"Start Thread :" + t.getName())
            t.setDaemon(True)
            t.start()
            tlst.append(t)

        for t in tlst:
            t.join()

    def write_content(self, content, content_range):
        self.file_lock.acquire()
        with open(self.filename, 'rb+') as f:
            f.seek(content_range[0])
            f.write(content)
        self.file_lock.release()

        self.fileinfo_lock.acquire()
        self.range_manager.set_written_range(content_range)
        self.fileinfo_lock.release()

    def read_next_range(self):
        self.fileinfo_lock.acquire()
        time.sleep(0.1)
        r = self.range_manager.get_unwritten_range()
        self.fileinfo_lock.release()
        return r

    def read_range_file(self):
        self.fileinfo_lock.acquire()
        manager = None
        if os.path.exists(self.fileinfo_name):
            log.info("read filename " + self.fileinfo_name)
            manager = DownloadWorkerThread.FileInfoManager(self.fileinfo_name, url=self.url)
            self.content_length = manager.get_total_length()
            if self.url.strip() == "":
                self.url = manager.url_in_file
        else:
            self.content_length = self.get_content_length()

            log.info("create filename_info length:" + str(self.content_length))
            with open(self.filename, "wb+") as f:
                f.seek(self.content_length)
            manager = DownloadWorkerThread.FileInfoManager(self.fileinfo_name, url=self.url,
                                                           filesize=self.content_length)
        self.fileinfo_lock.release()
        return manager

    def get_content_length(self):
        headers = self.headers
        headers['Range'] = "bytes=0-1"
        length = 0
        while length < 1024 * 1024 * 3:
            time.sleep(3)
            length = int(requests.get(self.url, headers=self.headers).headers['content-Range'].split('/')[1])
            log.info("Get length " + str(length))
        return length

    def RangeWorker(self, downloadWorker):
        while True:
            content_range = downloadWorker.read_next_range()
            if content_range == 0 and os.path.exists(self.fileinfo_name):
                os.remove(self.fileinfo_name)
                log.info(self.filename + " finished")
                break
            headers = downloadWorker.headers
            headers['Range'] = "bytes=" + str(content_range[0]) + "-" + str(content_range[1] - 1)
            while True:
                iTryTimes = 0
                r = requests.get(downloadWorker.url, headers=headers)
                if r.ok:
                    downloadWorker.write_content(r.content, content_range)
                    log.info("We are working on " + self.filename + " and now processing : " + \
                             str(round(1.0 * content_range[1] / self.content_length * 100, 2)) + "% in size " + str(
                        round(self.content_length / 1024.0 / 1024.0, 2)) + "MB.")
                    break
                else:
                    iTryTimes += 1
                    if iTryTimes > 1:
                        log.info("Downloading " + downloadWorker.url + " error. Now Exit Thread.")
                        return

    class FileInfoManager():
        url_in_file = ""
        writing_range = []
        written_range = []
        unwritten_range = []

        def __init__(self, filename, url="", filesize=0):
            self.filename = filename
            if not os.path.exists(filename):
                with open(filename, "w") as f:
                    f.write("unwritten_range=[(0," + str(filesize) + ")]\r\n")
                    f.write("writing_range=[]\r\n")
                    f.write("written_range=[]\r\n")
                    f.write("url_in_file=" + url)
                self.unwritten_range.append((0, filesize))
                self.url_in_file = url
            else:
                with open(filename, "r") as f:
                    for l in f.readlines():
                        typ = l.split("=")[0]
                        if typ == "writing_range":
                            typ = "unwritten_range"
                        elif typ == "url_in_file":
                            if url.strip() == "":
                                self.url_in_file = l.split("=")[1]
                            else:
                                self.url_in_file = url
                            continue
                        for tup in l.split("=")[1][1:-3].split('),'):
                            if tup == "":
                                continue
                            if tup.find("(") != 0:
                                tup = tup[tup.find("("):]
                            if tup.find(")") != 0:
                                tup = tup[:tup.find(")")]
                            getattr(self, typ).append( \
                                (int(tup.split(",")[0][1:]), int(tup.split(",")[1])))

        def get_total_length(self):
            if len(self.unwritten_range) > 0:
                return self.unwritten_range[-1][1]
            elif len(self.writing_range) > 0:
                return self.writing_range[-1][1]
            elif len(self.written_range) > 0:
                return self.written_range[-1][1]
            return 0

        def _save_to_file(self):
            with open(self.filename, "w") as f:
                f.write("writing_range=" + \
                        str(self.writing_range) + "\r\n")
                f.write("unwritten_range=" + \
                        str(self.unwritten_range) + "\r\n")
                f.write("written_range=" + \
                        str(self.written_range) + "\r\n")
                f.write("url_in_file=" + self.url_in_file)

        def _splice(self, intervals, newInterval):
            if len(intervals) == 0:
                return []
            intervals = self._concat(intervals, (0, 0))
            response = []
            for interval in intervals:
                if interval[0] == interval[1]:
                    continue
                if interval[0] > newInterval[1]:
                    response.append(interval)
                elif interval[1] < newInterval[0]:
                    response.append(interval)
                else:
                    max_range = (min(interval[0], newInterval[0]), max(interval[1], newInterval[1]))
                    if max_range != newInterval:
                        left = (min(max_range[0], newInterval[0]), max(max_range[0], newInterval[0]))
                        right = (min(max_range[1], newInterval[1]), max(max_range[1], newInterval[1]))
                        if left[0] != left[1]:
                            response.append(left)
                        if right[0] != right[1]:
                            response.append(right)
            return response

        def _concat(self, intervals, newInterval):
            if len(intervals) == 0:
                return [newInterval]
            response = [newInterval]
            for interval in intervals:
                i = response.pop()
                if interval[0] == interval[1]:
                    continue
                if i[0] > interval[1]:
                    response.append(interval)
                    response.append(i)
                elif i[1] < interval[0]:
                    response.append(i)
                    response.append(interval)
                else:
                    response.append((min(i[0], interval[0]), max(i[1], interval[1])))
            return response

        def get_unwritten_range(self, size=1024 * 1024):
            if len(self.unwritten_range) == 0:
                return 0
            r = self.unwritten_range[0]
            r = (r[0], min(r[0] + size, r[1]))
            self.unwritten_range = self._splice(self.unwritten_range, r)
            self.writing_range = self._concat(self.writing_range, r)
            self._save_to_file()
            return r

        def set_written_range(self, content_range):
            self.writing_range = self._splice(self.writing_range, content_range)
            self.written_range = self._concat(self.written_range, content_range)
            self._save_to_file()
