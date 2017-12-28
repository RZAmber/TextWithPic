#! /usr/bin/env python
# -*- coding utf-8 -*-

"""
@author:zhangrui
@file:img_content_clean.py
@time:2017/12/7 11:46
"""

import codecs

def get_imgID(filename):
    f = open(filename,'r')
    pic_id = []
    count = 0
    for line in f.readlines():
        pic_id.append(line.strip())
        count += 1
    return pic_id
def get_line(filename):
    f = codecs.open(filename, 'r','utf-8')
    lenth = len(f.readlines())
    return lenth

def get_imgINFO(filename_imginfo,filename_txt, filename_url, filename_imgurl, pic_id,lenth):
    f = codecs.open(filename_imginfo,'r','utf-8')
    f_txt = open(filename_txt,'w',errors='ignore',encoding='utf-8')
    f_url = open(filename_url,'w',encoding='utf-8')
    f_imgurl = open(filename_imgurl,'w',encoding='utf-8')
    i = 0
    imgID = ''
    text = []
    for t in range(lenth):
        print('processing line' + str(t))
        if i == 0:
            line = f.readline()
            line = line.split(' ')
            if line[0] in pic_id:
                imgID = line[0]
                img_url = line[2]
                f_imgurl.write(imgID + ' ' + img_url)
                i += 1
            else:
                for j in range(6):
                    f.readline()
                i = 0
        elif i in [1,2,3,4] and imgID != '':
            line = f.readline()
            text.append((line.strip().split('#'))[1])
            i += 1
        elif i == 5 and imgID != '':
            line = f.readline()
            url = (line.split('#'))[1]
            f_url.write(imgID + ' ' + url)
            f_txt.write(' '.join(text)+'\n')
            i=0
            text=[]

    f_url.close()
    f_imgurl.close()
    f_txt.close()
    f.close()


if __name__ == "__main__":

    filename = 'app/data/Tupianku_40K.txt'
    pic_id = get_imgID(filename)  # element 39678
    filename_imginfo = 'app/data/image_info.txt'
    filename_txt = 'app/data/img_text.txt'
    filename_url = 'app/data/img_texturl.txt'
    filename_imgurl = 'app/data/img_url.txt'
    get_imgINFO(filename_imginfo, filename_txt, filename_url, filename_imgurl, pic_id, get_line(filename_imginfo))