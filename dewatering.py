#coding: utf-8

from bs4 import BeautifulSoup
import re


class Dewatering(object):

    MIN_LENGTH = 200
    CONTENT_CLASSES = ("content", "article", "blog", "entry", "body", "post")

    def __init__(self, html):
        self.soup = BeautifulSoup(html)
        self.content = ''
        self._remove_useless_elems()

    def _remove_useless_elems(self):
        for style in self.soup.find_all('style'):
            style.extract()
        for style in self.soup.find_all('script'):
            style.extract()
        for style in self.soup.find_all('link'):
            style.extract()

    def _set_content(self, article):
        if len(article) < Dewatering.MIN_LENGTH:
            return False
        if len(article) < len(self.content):
            return False
        self.content = unicode(article)

    def _search_article_tag(self):
        article = self.soup.article
        if article:
            self._set_content(article)

    def _search_div(self):
        for kls in Dewatering.CONTENT_CLASSES:
            tags = self.soup.find_all("div", {"class": re.compile(kls)})

            for tag in tags:
                self._set_content(tag)
