#! /usr/bin/env python
# -*-coding:utf-8 -*-

"""
@author:zhangrui
@file:TextPic.py
@time:2017/12/8 15:13
"""

from gensim import corpora, models, similarities
import logging
from basic_parse import process4input

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class TextPic:
    def __init__(self):
        dictionary_path = 'app/model/dictionary.dict'
        tfidf_model_path = 'app/model/model.tfidf'
        index_lsi_path = 'app/model/lsi.index'
        self.dictionary = corpora.Dictionary.load(dictionary_path)
        self.tfidf = models.TfidfModel.load(tfidf_model_path)

        lsi_model_path = 'app/model/model.lsi'
        self.lsi = models.LsiModel.load(lsi_model_path)
        self.index = similarities.MatrixSimilarity.load(index_lsi_path)

        ##Try to train Lda model instead of Lsi with gensim library. It's the same way as train_lsi.py
        # index_lda_path = 'app/model/lda.index'
        # lda_model_path = 'app/model/model.lda'
        # self.lda = models.LsiModel.load(lda_model_path)

    def run(self,sentence):
        filename = 'app/data/img_url.txt'
        filename1 = 'app/data/img_texturl.txt'
        img_url = self.__g_imgurl(filename)
        img_text_url = self.__g_it_Url(filename1)

        query = process4input(sentence)
        query_bow = self.dictionary.doc2bow(query)
        query_bow = sorted(list(query_bow), key = lambda item: -item[-1])[:10]
        query_tfidf = self.tfidf[query_bow]
        query_tfidf = sorted(list(query_tfidf), key=lambda item: -item[-1])[:5]

        query_lsi = self.lsi[query_tfidf]
        sims = self.index[query_lsi]

        sims = sorted(enumerate(sims), key = lambda item: -item[-1])[:20]

        url = []

        for item in sims:
            temp = {}
            img_num = int(item[0])
            temp['imgurl'] = img_url[img_num]
            temp['imgtext'] = img_text_url[img_num]
            url.append(temp)
        return url

    def __g_imgurl(self,filename):
        img_url = []
        f = open(filename, 'r')
        data = f.readlines()
        for line in data:
            line = line.strip().split(' ')
            img_url.append(line[1])
        f.close()
        return img_url

    def __g_it_Url(self,filename):
        img_text_url = []
        f = open(filename, 'r')
        data = f.readlines()
        i = 0
        for line in data:
            line = line.strip().split(' ')
            if len(line) == 2:
                img_text_url.append(line[1])
            else:
                img_text_url.append(' ')
        f.close()
        return img_text_url






if __name__ == "__main__":
    sentence = "屠宰环节一头连着畜禽养殖，一头连着肉品消费，是保障肉品质量安全的关键一环。记者从第二届全国屠宰加工标准化技术委员会成立大会上获悉：自屠宰监管职责调整以来，农业部推进畜禽屠宰行业管理，开展重要标准制修订，屠宰标准化工作取得明显成效。目前已梳理1000余项标准，完成129项推荐性标准的集中复审，制修订近30项畜禽屠宰国家标准和行业标准，加快屠宰行业绿色发展、转型发展。" \
               "农业部副部长于康震在会上表示，当前正处在屠宰行业转型升级的关键时期，要补齐短板，织密屠宰标准体系网络，构建以国家标准、行业标准为主体，地方标准、团体标准和企业标准为补充，强制性标准和推荐性标准协同配合的标准体系。"
    textpic = TextPic()

    data = textpic.run(sentence)
    print(data)



