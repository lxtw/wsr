# -*- coding: utf-8 -*-
import scrapy


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/new100.html']
    
    def parse(self, response):
        items=[]
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            name = each_movie.xpath('./h5/a/@title').extract()[0]
            items.append(name)
        with open("my_meiju.txt",'w') as fp:
            for each in items: 
                fp.write(each+'\n')     
        return items
