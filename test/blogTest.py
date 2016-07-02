#encoding=utf-8

import urllib2
import time
import random

def getPage(url):
    try:
        timeout = 5
        request = urllib2.Request(url)
        #伪装HTTP请求
        request.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
        request.add_header('connection','keep-alive')
        request.add_header('referer', url)
        # request.add_header('Accept-Encoding', 'gzip')  # gzip可提高传输速率，但占用计算资源
        response = urllib2.urlopen(request, timeout = timeout)
        html = response.read()
        #if(response.headers.get('content-encoding', None) == 'gzip'):
        #    html = gzip.GzipFile(fileobj=StringIO.StringIO(html)).read()
        response.close()
        return html
    except Exception as e:
        print 'URL Request Error:', e
        return None


if __name__ == '__main__':
    url = 'http://blog.csdn.net/wds2006sdo/article/details/51210896'

    for i in range(5000):
        html = getPage(url)

        # 随机睡眠1~60秒
        sleep_time = random.randint(1,60)
        print i,' sleep ',sleep_time,' second'
        time.sleep(sleep_time)