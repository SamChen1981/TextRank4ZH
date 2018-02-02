#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

import tornado.ioloop
import tornado.web
import json
import urllib
import codecs
from textrank4zh import TextRank4Sentence
from textrank4zh import TextRank4Keyword

class WordRank(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        res = TextRankWord(json.loads(self.request.body))
        self.write(json.dumps(res))

class TextRank(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        #print self.request.body
        #print json.loads(self.request.body)
        res = TextRankSentence(json.loads(self.request.body))
        self.write(json.dumps(res))

class KeyphrasesRank(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        res = TextRankKeyphrases(json.loads(self.request.body))
        self.write(json.dumps(res))

def TextRankKeyphrases(input):

    text = input['content']
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, lower=True, window=3, pagerank_config={'alpha': 0.85})
    result = tr4w.get_keyphrases(30, word_min_len=2)
    # for item in tr4s.get_key_sentences(num=5):
        # result['sentence'] = item.sentence
        # print(item.index, item.weight, item.sentence)
    return result


def TextRankSentence(input):

    text = input['content']
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    result = tr4s.get_key_sentences(num=5)
    # for item in tr4s.get_key_sentences(num=5):
        # result['sentence'] = item.sentence
        # print(item.index, item.weight, item.sentence)
    return result

def TextRankWord(input):

    text = input['content']
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, lower=True, window=3, pagerank_config={'alpha': 0.85})
    result = tr4w.get_keywords(30, word_min_len=2)
    # for item in tr4s.get_key_sentences(num=5):
        # result['sentence'] = item.sentence
        # print(item.index, item.weight, item.sentence)
    return result

application = tornado.web.Application([
    (r"/TextRank", TextRank),
    (r"/WordRank", WordRank),
    (r"/KeyphrasesRank", KeyphrasesRank),
])

if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
