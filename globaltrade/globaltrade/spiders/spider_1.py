# -*- coding: utf-8 -*-
import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider_1'
    allowed_domains = ['www.globaltrade.net']
    start_urls = [
    'https://www.globaltrade.net/international-trade-import-exports/expert-service-provider-p/Fastfix-Inc.html'
    ]

    def parse(self, response):
    	yield{
    	# 'logo_url': response.css(".image .lazy::text").extract_first(),
    	'title': response.css(".sp-title span::text").extract_first(),
    	'sub_title': response.css(".sub::text").extract_first(),
    	'primary_location': response.css('.profile-details span span::text').extract_first(),
    	'area_of_expertise': response.css(".mainExp::text").extract_first(),
    	'about': response.css(".details p::text").getall(),
    	'website': response.css(".details a:nth-child(1)::text").extract_first(),
    	'languages_spoken': response.css("tr:nth-child(5) td+ td::text").extract_first(),
    	# 'page_url': response.css(".sp-title span::text").extract_first(),
    	}
        
