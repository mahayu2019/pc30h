#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import re

# 模式修正符
'''
I 匹配时忽略大小写 *重点
M 多行匹配 *
L 本地化识别匹配
U unicode
S 让.匹配包括换行符 *
'''

str='Python'
pat='pyt'
rs=re.search(pat,str,re.I)
print(rs)
