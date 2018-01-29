#! /usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

import tornado.ioloop
import tornado.web
import json
import urllib
import codecs
from textrank4zh import TextRank4Sentence


class TextRank(tornado.web.RequestHandler):
    def get(self):
        pass
    def post(self):
        #print self.request.body
        #print json.loads(self.request.body)
        res = TextRankSentence(json.loads(self.request.body))
        self.write(json.dumps(res))

def TextRankSentence(input):

    text = input['content']
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    result = tr4s.get_key_sentences(num=5)
    # for item in tr4s.get_key_sentences(num=5):
        # result['sentence'] = item.sentence
        # print(item.index, item.weight, item.sentence)
    return result

application = tornado.web.Application([
    (r"/TextRank", TextRank),
])

if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
