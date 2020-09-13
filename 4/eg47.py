#!/usr/bin/env python
# coding=utf-8

import re
import urllib.request

url = 'https://news.qq.com'
#data = urllib.request.urlopen(url).read().decode('gb2312')
data = urllib.request.urlopen('https://news.qq.com').read().decode('utf-8')

print(data)
