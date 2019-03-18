# -*- coding: utf-8 -*-
import scrapy
from movie1.items import Movie1Item
 
class Meiju1Spider(scrapy.Spider):
    name = "meiju1"
    allowed_domains = ["meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']
 
    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = Movie1Item()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            print(item) 
            yield item
