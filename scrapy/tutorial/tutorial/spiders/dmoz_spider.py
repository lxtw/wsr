import scrapy
from tutorial.items import DmozItem
class DmozSpider(scrapy.Spider):
    name="dmoz"
    allowed_domains=["dmoz.org"]
    start_urls=[ 'http://www.dmozdir.org/About/', 'http://www.dmozdir.org/News/' ]
    def parse(self,response):
        items=[]
        sel=scrapy.selector.Selector(response)
        sites=sel.xpath('//li/li')
       
        for site in sites:
            item=DmozItem()
            item['title']=site.xpath('a/text()').extract()
            
            items.append(item)

        return items
