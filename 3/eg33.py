#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import re

# 元字符
'''
. 除换行符外任意字符
^ 开始位置
$ 结束位置
* 0-1-多次
? 0-1次
+ 1-多次
{n} 恰好n次
{n,} 最少出现n次
{n,m} 最少n次,最多m次
| 或
() 模式单元
'''
string = '''taoyunnnnji9886565askdwjqejyunnnnnnlkqjbaidu'''
pat = 'tao...'
pat='^ao...'
pat='bai..$'
pat='tao.*'
pat='8+'
pat='988?'
pat='yun{3,}'
pat='yun{5,70}'
rst = re.search(pat, string)
print(rst)
