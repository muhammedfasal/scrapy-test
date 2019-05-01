# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
import json
import re


class Spider1Spider(scrapy.Spider):
    name = 'spider_1'
    allowed_domains = ['www.globaltrade.net']
    start_urls = [
    'https://www.globaltrade.net/United-States/expert-service-provider.html?pageSize=10&orderBy=1&filterByPost=false&filterByRef=false&topicClear=false&industryClear=false&currentPage=%s'
    % page for page in range(0,100)
    ]

    def parse(self, response):
    	urls = response.css('.profileNavigator::attr(href)').extract()
    	for url in urls:
    		url = response.urljoin(url)
    		yield scrapy.Request(url=url, callback=self.parse_detials)

    	#pagination
    	next_page_url = response.css('.next-page::attr(href)').extract_first()
    	if next_page_url is not None:
    		next_page_url = response.urljoin(next_page_url)
    		yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detials(self, response):
    	about1 = response.css(".details td p::text").getall()
    	about2 = ''.join(about1)
    	about3 = about2.replace("\n", "")
    	languages_spoken1 = str(response.css("tr:nth-child(5) td+ td::text").extract_first())
    	languages_spoken2 = languages_spoken1.replace("\n","")
    	primary_location1 = str(response.css('.profile-details span span::text').extract_first())
    	primary_location2 = primary_location1.replace("\n","")
    	website1 = str(response.css(".details a:nth-child(1)::text").extract_first())
    	website2 = website1.replace("\n","")
    	dataset = {
    	'logo_url': response.css('.image .lazy::attr(data-original)').extract_first(),
    	'title': response.css(".sp-title span::text").extract_first(),
    	'sub_title': response.css(".sub::text").extract_first(),
    	'primary_location': primary_location2,
    	'area_of_expertise': response.css(".mainExp::text").extract_first(),
    	'about': about3,
    	'website': website2,
    	'languages_spoken': languages_spoken2,
    	'page_url': response.url,
    	}
    	yield dataset

        
