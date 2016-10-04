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
            return html.decode('gbk')
        except Exception as e:
            print 'URL Request Error:', e
            return None



    def get_workable_ip(self):

        for i in xrange(1,self.__pages+1):
            url = self.__ip_bank_url % i
            print self.access_by_url(url)
            break

if __name__ == '__main__':
    p = Proxy()
    p.get_workable_ip()
