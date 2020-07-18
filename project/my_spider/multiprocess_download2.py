def download_big_file(url, target_file_name):
    """
        使用python核心库下载大文件
        ref: https://stackoverflow.com/questions/1517616/stream-large-binary-files-with-urllib2-to-file
    """
    import sys
    if sys.version_info > (2, 7):
        # Python 3
        from urllib.request import urlopen
    else:
        # Python 2
        from urllib2 import urlopen

    response = urlopen(url)
    chunk = 16 * 1024
    with open(target_file_name, 'wb') as f:
        while True:
            chunk = response.read(chunk)
            if not chunk:
                break
            f.write(chunk)