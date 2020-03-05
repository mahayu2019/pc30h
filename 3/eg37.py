#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import re

# 正则实例
# 1.匹配.com和.cn网址
string = "<a href='http://www.baidu.com'>百度</a>"
pat='[a-zA-Z]+://[^\s]*[.com|.cn]'
rs=re.compile(pat).findall(string)
print(rs)
