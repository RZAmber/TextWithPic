#! /usr/bin/env python
#-*-coding:utf-8 -*-

"""
@author:zhangrui
@file:basic_parse.py
@time:2017/12/8 9:47
"""

import os
import jieba
import codecs
import jieba.posseg as pseg
import gc


def check2skip(filename):
    if os.path.exists(filename):
        return 1
    return 0

class Parse:

    def __init__(self, filename = '', userdic_file = ''):
        self.text = ''
        if filename != '':
            data = codecs.open(filename,'r',encoding='utf8').readlines()
            self.text = [line.strip() for line in data]
        if userdic_file != '':
            jieba.load_userdict(userdic_file)

    def parse(self, sentence):
        seg_list = jieba.lcut(sentence)
        return seg_list

    def POStag(self, sentence):
        tag = ['n','nr','ns','nt','nz','s','vn']
        tag_non = ['q']
        words = pseg.cut(sentence)
        seg_list = []
        for word, flag in words:
            if flag in tag not in tag_non:
                seg_list.append(word)
        return seg_list

    def parse_text(self):
        parse_text = []
        text = self.text
        total_line = len(text)
        for i, sentence in enumerate(text):
            if i%1000 == 0:
                print("parse: %d/%d..."%(i,total_line))
            seg_list = self.POStag(sentence)
            parse_text.append(seg_list)
        return parse_text

class Clean:
    def __init__(self, stopwords_file = 'app/data/stopwords.txt', punc_file = 'app/data/punctuation.txt'):
        stopwords = set([word.strip() for word in open(stopwords_file,'r',encoding='utf8').readlines()])
        punc = [x.strip() for x in open(punc_file,'r',encoding='utf8').readlines()]
        self.stopwords = stopwords
        self.punc = set(punc +['\t'] + [' '])

    def del_stopwords(self,words):
        clean_words = [word for word in words if word not in self.stopwords]
        return clean_words

    def del_punwords(self,words):
        clean_words = [word for word in words if word not in self.punc]
        return clean_words


def preProcess(filename):
    parse = Parse(filename)
    parse_text = parse.parse_text()
    clean = Clean()
    clean_sentence = []

    for i, words in enumerate(parse_text):
        words = clean.del_stopwords(words)
        words = clean.del_punwords(words)
        clean_sentence.append(words)
        if i%1000 == 0:
            print(i)

    print("del ...")
    del parse
    del clean
    gc.collect()

    return clean_sentence

def process4input(sentence):
    parse = Parse()
    seg_list = parse.POStag(sentence)
    clean = Clean()
    seg_list = clean.del_stopwords(seg_list)
    seg_list = clean.del_punwords(seg_list)

    print("del ...")
    del parse
    del clean
    gc.collect()

    return seg_list

if __name__ == "__main__":
    filename = 'app/data/img_text.txt'
    clean_sentence1 = preProcess(filename)

    clean = Clean()
    clean_sentence = []
    for i, words in enumerate(clean_sentence1):
        words = clean.del_stopwords(words)
        words = clean.del_punwords(words)
        clean_sentence.append(words)
        if i%1000 == 0:
            print(i)
    print(clean_sentence[0:5])









