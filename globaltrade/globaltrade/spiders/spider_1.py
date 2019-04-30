# -*- coding: utf-8 -*-
import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider_1'
    allowed_domains = ['www.globaltrade.net']
    start_urls = ['http://www.globaltrade.net/']

    def parse(self, response):
        pass
