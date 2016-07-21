#encoding=utf-8

import re
import urllib2
import time
import random
import codecs

class CSDN(object):
    basic_url = 'http://blog.csdn.net/wds2006sdo/article/list/%d'

    try_times = 1
    sleep_time = 10
    run_times = 30

    base_url = 'http://10.0.10.66/cgi-bin/srun_portal?username=%s&password=%s&action=login&ac_id=3'
    test_url = 'http://www.baidu.com'

    def init(self):
        self.blogs = self.get_pages()
        self.add_eachblog_random_range()
        self.random_range = self.blogs[-1][2]


        for blog in self.blogs:
            print blog[0], ' ' ,blog[1],' ',blog[2]

    def is_network_accessable(self):

        for i in range(self.try_times):
            html = self.access_by_url(self.test_url)
            if not html:
                continue

            if '百度' in html:
                print 'network workable!'
                return True

            time.sleep(self.sleep_time)

        print 'network not work!'
        return False


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

    def get_pages(self):
        suffix = ''
        blog_list = []
        page = 1
        lastpage = 2

        while page <= lastpage:
            url = self.basic_url % page
            html = self.access_by_url(url)

            thispage_blogs = self.extract_blogs(html)
            blog_list.extend(thispage_blogs)

            try:
                lastpage = int(re.findall('<a href=.*?(\d)">尾页',html)[0])
            except:
                break

            page += 1

        return blog_list

    def extract_blogs(self,html):
        blogs = []
        blog_strings = re.findall('<span class="link_view" title="阅读次数">.*</span>',html)

        for blog_string in blog_strings:
            url = 'http://blog.csdn.net/wds2006sdo/article/details/' + re.findall('wds2006sdo/article/details/(\d+)',blog_string)[0]
            read_count = re.findall('\((\d+)\)',blog_string)[0]
            blogs.append([url,int(read_count)])

        return blogs

    def write_file(self,content):
        file_object = codecs.open("index.html",'w')
        file_object.write(str(content))
        file_object.close()

    def add_eachblog_random_range(self):
        sum = 0
        for blog in self.blogs:
            sum += blog[1]

        mean = int(float(sum) / float(len(self.blogs)))
        order_num = mean * 100

        end = 0
        for blog in self.blogs:
            blog.append(end+mean+order_num)
            end += mean+order_num
            order_num = int(order_num ** 0.5)

    def select_page(self):
        num = random.randint(1,self.random_range)
        print 'num ',num
        i = 0
        while i < len(self.blogs) and num > self.blogs[i][2]:
            i += 1

        return self.blogs[i][0]

    def sleep(self):
        sleep_time = random.randint(1,60)
        print ' sleep ',sleep_time,' second'
        time.sleep(sleep_time)

    def robot_start(self):
        if not self.is_network_accessable():
            return

        self.init()

        for i in range(self.run_times):
            url = self.select_page()
            print url
            self.access_by_url(url)
            self.sleep()


if __name__ == '__main__':
    csdn = CSDN()
    csdn.robot_start()




