#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import re

# 正则表达式函数
# 1.match--从头开始匹配
str = 'pythonabc123'
pat = 'py'
rs = re.match(pat, str)
print(rs)

# 2.search--全位置匹配

# 3.全局匹配函数--re.compile(正则表达式).findall(目标字符串)
str='asjdhqwielkasdlkkdhffsasdjjw'
pat='a.*?d'
rs=re.compile(pat).findall(str)
print(rs)