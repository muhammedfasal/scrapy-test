# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin


class Spider1Spider(scrapy.Spider):
    name = 'spider_1'
    allowed_domains = ['www.globaltrade.net']
    start_urls = [
    'https://www.globaltrade.net/United-States/expert-service-provider.html?pageSize=10&orderBy=1&filterByPost=false&filterByRef=false&topicClear=false&industryClear=false&currentPage=%s'
    % page for page in range(1,100)
    ]

    def parse(self, response):
    	urls = response.css('.profileNavigator::attr(href)').extract()
    	for url in urls:
    		url = response.urljoin(url)
    		yield scrapy.Request(url=url, callback=self.parse_detials)

    	#pagination
    	next_page_url = response.css('.next-page::attr(href)').extract_first()
    	if next_page_url:
    		next_page_url = response.urljoin(next_page_url)
    		yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detials(self, response):
    	dataset = {
    	'logo_url': response.css('.image .lazy::attr(data-original)').extract_first(),
    	'title': response.css(".sp-title span::text").extract_first(),
    	'sub_title': response.css(".sub::text").extract_first(),
    	'primary_location': response.css('.profile-details span span::text').extract_first(),
    	'area_of_expertise': response.css(".mainExp::text").extract_first(),
    	'about': response.css(".details p::text").getall(),
    	'website': response.css(".details a:nth-child(1)::text").extract_first(),
    	'languages_spoken': response.css("tr:nth-child(5) td+ td::text").extract_first(),
    	'page_url': response.url,
    	}
    	yield dataset
        
