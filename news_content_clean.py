#! /usr/bin/env python
#-*-coding:utf-8 -*-

"""
@author:zhangrui
@file:news_content_clean.py
@time:2017/12/7 10:10
"""
import re
import codecs

def CleanContent(filename, filename_new):
    f = codecs.open(filename,'r','utf-8')
    f_clean = open(filename_new, 'w', encoding='utf-8')
    I= 0
    for i in range(20000):
        line = f.readline()
        dr = re.compile(r'<.*?>', re.S)
        clean_line = dr.sub('', line)
        clean_line = clean_line.split(' ')[1:]
        f_clean.write(' '.join(clean_line))
        if i % 1000 == 0:
            print(i)

    f_clean.close()
    f.close()

if __name__ == '__main__':
    filename = 'app/data/news_content.txt'
    filename_new = 'app/data/news_content_clean.txt'
    CleanContent(filename,filename_new)
