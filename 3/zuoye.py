#!/usr/bin/env python
# coding=utf-8
import pretty_errors
import requests
import re


# 作业题:提取豆瓣出版社列表名单
# 应对反爬虫机制,提取页面
def get_page_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


url = "https://read.douban.com/provider/all"
data = get_page_html(url)
pat = '<div class="name">(.*?)</div>'
rs = re.compile(pat).findall(data)
# 存入文件
filename = 'cbsml.txt'
with open(filename, 'w') as file_object:
    for t in rs:
        file_object.write(t+'\n')


