#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:zhangrui
@file:test.py
@time:2017/12/18 14:34
"""

from gensim import models
from basic_parse import preProcess


filename = 'app/data/img_text.txt'
clean_sentence_img = preProcess(filename)[:20]
train_corpus = []
for line,i in enumerate(clean_sentence_img):
    train_corpus.append(models.doc2vec.TaggedDocument(line, [i]))

model = models.doc2vec.Doc2Vec(size=50, min_count=2, iter=55)
model.build_vocab(train_corpus)
model.train(train_corpus)
test = ['屠宰', '环节', '畜禽', '养殖', '肉品', '消费', '肉品', '质量', '关键', '环', '全国', '屠宰', '加工', '标准化', '技术', '委员会', '大会', '屠宰', '监管', '职责', '调整', '农业部', '畜禽', '屠宰', '行业', '管理', '标准制', '屠宰', '标准化', '工作', '标准', '项', '推荐性', '标准', '制', '项', '畜禽', '屠宰', '国家标准', '行业标准', '屠宰', '行业', '绿色', '发展', '转型', '发展', '农业部', '部长', '于康震', '屠宰', '行业', '转型', '升级', '关键时期', '短板', '织密', '屠宰', '标准', '体系', '网络', '国家标准', '行业标准', '主体', '地方', '标准', '团体', '标准', '企业', '标准', '强制性', '标准', '推荐性', '标准', '协同', '标准', '体系']
inferred_vector = model.infer_vector(test)
sims = model.docvecs.most_similar([inferred_vector], topn=3)
print(sims)