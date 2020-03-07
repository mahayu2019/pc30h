#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import re

# 正则实例
# 1.匹配.com和.cn网址
string = "<a href='https://pic.wej.google.com'>百度</a>"
pat = '[a-z]+://[a-z].*[.com|.cn|.org]'
rs = re.compile(pat).findall(string)
print(rs)

# 2.匹配电话号码
str = 'tel:021-12345678,tel2:010-95271,tel3:0512-585415579'
pat = '\d{3,4}-\d{5,8}'
rs = re.compile(pat).findall(str)
print(rs)


# DIY 提取网址函数
def geturl(url):
    pat = '[a-z]+://[a-z].*.com'
    rs = re.compile(pat).findall(url)
    return rs


g = '''
<a href="http://news.baidu.com" target="_blank" class="mnav">新闻</a>
<a href="https://www.hao123.com" target="_blank" class="mnav">hao123</a>
<a href="http://map.baidu.com" target="_blank" class="mnav">地图</a>
<a href="http://v.jweu.baidu.com" target="_blank" class="mnav">视频</a>
<a href="http://wsd.tieba.baidu.com" target="_blank" class="mnav">贴吧</a>
<a href="http://xueshu.baidu.com" target="_blank" class="mnav">学术</a>
'''
t = geturl(g)
# print(t)
