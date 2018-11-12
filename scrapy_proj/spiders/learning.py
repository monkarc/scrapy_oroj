# -*- coding: utf-8 -*-
import scrapy


class LearningSpider(scrapy.Spider):
    name = 'learning'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def parse(self, response):
        pass
