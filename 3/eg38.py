#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import urllib.request
import re

# 简单爬虫的编写
#.decode('utf-8') 转为文本格式
data = urllib.request.urlopen('https://edu.csdn.net/huiyiCourse/detail/253').read().decode('utf-8')
pat = '<p>(\d+)</p>'
rs = re.compile(pat).findall(data)
print(rs[0])
