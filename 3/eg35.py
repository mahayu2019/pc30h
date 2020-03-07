#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import re

'''
贪婪模式:尽可能多的匹配  .*
懒惰模式:尽可能少的匹配  .*?
'''

str = 'pythonaybc123o'
# 贪婪模式
pat1 = 'p.*o'  # 从第一个字符匹配到最后一个可对应的字符,中间重复都忽略,模糊查找
# 懒惰模式
pat2 = 'p.*?o'  # 从第一个字符匹配到第一个可对应的字符立即终止,精准查找
rs = re.search(pat1, str)
rs2 = re.search(pat2, str)
print(rs)
print(rs2)
