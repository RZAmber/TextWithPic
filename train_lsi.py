#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:zhangrui
@file:train_lsi.py
@time:2017/12/8 13:14
"""

from gensim import corpora, models, similarities
from basic_parse import preProcess
import logging
import time
import gc

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class Dictionary(object):
    def __init__(self, sentences, dictionary_path):
        self.sentences = sentences
        self.dictionary_path = dictionary_path

    def build(self):
        dictionary = corpora.Dictionary(self.sentences)
        dictionary.filter_extremes(no_above = 50)
        corpora.Dictionary.save(dictionary, self.dictionary_path)

        return dictionary

class ge_tfidf:
    def __init__(self, data, dictionary,tfidf_model_path):
        self.dictionary = dictionary
        self.data = data
        self.tfidf_model_path = tfidf_model_path


    def __iter__(self):
        for sentence in self.data:
            yield self.dictionary.doc2bow(sentence)

    def build(self):
        tfidf = models.TfidfModel(self)
        tfidf.save(self.tfidf_model_path)
        return tfidf


class Train_LSI:
    def __inti__(self):
        pass
    def run(lsi_model_path, tfidf_vector, num_topics, id2word):
        lsi = models.LsiModel(tfidf_vector,id2word=id2word, num_topics = num_topics)
        lsi.save(lsi_model_path)

        return lsi


def main(*clean_sentence):
    start = time.time()

    sentences = []
    clean_sentence_img = []
    for i,c in enumerate(clean_sentence):
        if i == 0:
            clean_sentence_img = c
        sentences += c

    lsi_model_path = 'app/model/model.lsi'
    dictionary_path = 'app/model/dictionary.dict'
    tfidf_model_path = 'app/model/model.tfidf'
    num_topics = 200

    dictionary = Dictionary(sentences,dictionary_path).build()
    tfidf = ge_tfidf(sentences, dictionary,tfidf_model_path).build()

    corpus_all = [dictionary.doc2bow(sentence) for sentence in sentences]
    tfidf_vector = tfidf[corpus_all]

    del corpus_all
    del sentences
    gc.collect()

    lsi = Train_LSI.run(lsi_model_path,tfidf_vector,num_topics,dictionary)
    del tfidf_vector
    gc.collect()

    corpus = [dictionary.doc2bow(sentence) for sentence in clean_sentence_img]
    tfidf_vector_img = tfidf[corpus]
    del clean_sentence_img
    del corpus
    gc.collect()

    index_lsi = similarities.MatrixSimilarity(lsi[tfidf_vector_img])
    index_lsi.save('app/model/lsi.index')

    del tfidf_vector_img
    gc.collect()

    end = time.time()
    print("running time " + str(end-start))



if __name__ == "__main__":
    filename = 'app/data/img_text.txt'
    filename_add = 'app/data/news_content_clean.txt'
    clean_sentence_img = preProcess(filename)
    clean_setnence_new = preProcess(filename_add)
    main(clean_sentence_img,clean_setnence_new)