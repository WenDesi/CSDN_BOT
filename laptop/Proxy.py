#encoding=utf-8

import urllib2
import random
import time
import lxml
import re

class Proxy(object):

    def __init__(self):
        self.__deadline = 3
        self.__pages = 10
        self.__ip_bank_url = 'http://www.ip181.com/daili/%d.html'

    def access_by_url(self,url):
        try:
            timeout = 5
            request = urllib2.Request(url)

            #伪装HTTP请求
            request.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
            request.add_header('connection','keep-alive')
            request.add_header('referer', url)

            response = urllib2.urlopen(request, timeout = timeout)
            html = response.read()

            response.close()
            return html
        except Exception as e:
            print 'URL Request Error:', e
            return None

    def __get_html(self,url):
        headers = {
                'Host': 'www.ip181.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Referer': r'http://www.ip181.com/daili/1.html',
                }

        req = Request(url,headers=headers)
        print url
        html = None
        try:
            html = urlopen(req,timeout = 5).read().decode('utf-8')
        except Exception as e:
            print '******打开失败！******'
        print html


    def get_workable_ip(self):

        for i in xrange(1,self.__pages+1):
            url = self.__ip_bank_url % i
            print self.access_by_url(url)
            break

if __name__ == '__main__':
    p = Proxy()
    p.get_workable_ip()
