# -*- coding: gbk -*-
import scrapy
from scrapy import Request

from dcpq.items import DcpqItem


class AppendixSpider(scrapy.Spider):
    name = "appendix"
    allowed_domains = ['ches.org.cn']
    start_urls = ['http://www.ches.org.cn/ches/slkp/slkpsy/']
    def parse(self, response):
        title_list = response.xpath("/html/body/div[5]/div/div[1]/div[2]/ul/li/a/p/text()").extract()
        url_list = response.xpath("/html/body/div[5]/div/div[1]/div[2]/ul/li/a/@href").extract()
        for i, j in zip(title_list, url_list):           
            dcpq = DcpqItem()
            dcpq['type'] = i
            url ='http://www.ches.org.cn/ches' + j[5:] + '/'
            yield scrapy.Request(url, callback=self.title_parse, meta={'item': dcpq, 'url': url})
            print(i, ':', url)

    def title_parse(self, response):
        dcpq = response.meta['item']
        dcpqurl = response.meta['url']
        title_list = response.xpath("/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div/div/div[1]/h5/a/text()").extract()
        url_list = response.xpath("/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div/div/div[1]/h5/a/@href").extract()
        time_list = response.xpath("/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div/div/div[2]/h6/text()").extract()
        
        for title, url, time in zip(title_list, url_list, time_list):
            dcpq['title'] = title
            dcpq['pubTime'] = time
            url = dcpqurl + url[2:]
            dcpq["url"]=url
            print(title, ':', time, ':', url)
            if url[len(url)-3:]!="pdf":
                yield scrapy.Request(url, callback=self.content_parse, meta={'item': dcpq})
            
    def content_parse(self, response):

        dcpq = response.meta['item']
        content = response.xpath('string(//div[@class="row"]/div/div/h3[@style="line-height:40px;"])').extract()
        if content!=[]:
            content=content[0]
            print(content)
            dcpq['content'] = content
            yield dcpq

    
