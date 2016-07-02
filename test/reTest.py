#encoding=utf-8

import re


if __name__ == '__main__':
    string = 'masdfasdfasdkljfiemf下一页'
    print re.findall('m*?下一页',string)