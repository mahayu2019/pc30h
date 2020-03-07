#!/usr/bin/env python
# coding=utf-8
# import pretty_errors
import urllib.request

# 1.urlretrieve 下载网页到本地
url = 'http://www.163.com'
urllib.request.urlretrieve(url, 'd.html')

# 2.urlcleanup() 清理缓存
urllib.request.urlcleanup()

# 3.info() 查看网页简介信息
file = urllib.request.urlopen('http://www.163.com')
print(file.info())

# 4.getcode() 获得状态码
print(file.getcode())

# geturl() 当前所在页面
print(file.geturl())