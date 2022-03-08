# from ast import Yield
# from turtle import title

import scrapy
from ..items import SeamsfriendlyItem

class ShortsSpider(scrapy.Spider):
    name = 'shorts'
    start_urls = ['https://in.seamsfriendly.com/collections/shorts?page=1']
    page_num=2
    max_page=4

    def parse_prod(self, response):
        item = SeamsfriendlyItem()

        title = response.css(".u-h2::text").get().replace('\n' , '').strip()
        ImgLinks = ["https:"+i for i in response.css(".Product__Slideshow .Product__SlideItem--image div img").css("::attr(data-original-src)").extract()]
        price = response.css("#shopify-section-product-template .Price").css("::text").get().replace('₹', '').replace(',', '')
        description = '\n'.join(response.css(".Rte ul li::text").extract()[9:])


        item['title'] = title
        item['ImgLinks'] = ImgLinks
        item['price'] = price
        item['description'] = description


        yield item

    
    def parse(self, response):
        
        for link in response.css(".ProductItem .ProductItem__Wrapper").css("a::attr(href)"):
            yield response.follow(link.get(),  callback=self.parse_prod)
       
        
        next_page = "https://in.seamsfriendly.com/collections/shorts?page=" +str(ShortsSpider.page_num)+""

        if ShortsSpider.page_num < ShortsSpider.max_page:
            # print("\n\n\n\nNEXT PAGE :****************************", next_page, "*****************")
            ShortsSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)

   




# color
# response.css(".swatch-group-selector.swatch-custom-image").css("::attr(orig-value)").extract()

             

