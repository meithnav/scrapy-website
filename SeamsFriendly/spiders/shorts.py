# from ast import Yield
# from turtle import title

import scrapy
from ..items import SeamsfriendlyItem

class ShortsSpider(scrapy.Spider):
    name = 'shorts'
    start_urls = ['https://in.seamsfriendly.com/collections/shorts?page=1/']
    page_num=1
    max_page=4

    def parse_prod(self, response):
        item = SeamsfriendlyItem()

        title = response.css(".u-h2::text").get().replace('\n' , '').strip()
        ImgLinks = response.css(".Product__Slideshow .Product__SlideItem--image div img").css("::attr(data-src)").extract()
        price = response.css("#shopify-section-product-template .Price").css("::text").get().replace('₹', '').replace(',', '')
        description = '\n'.join(response.css(".Rte ul li::text").extract()[9:])


        item['title'] = title
        item['ImgLinks'] = ImgLinks
        item['price'] = price
        item['description'] = description


        yield item

    
    def parse(self, response):
        
        all_shorts_links = response.css(
            ".ProductItem .ProductItem__Wrapper").css("a::attr(href)")

        for link in all_shorts_links:
            yield response.follow(link.get(),  callback=self.parse_prod)

            

    
    # def parse(self, response):


    #     next_page = 'https://in.seamsfriendly.com/collections/shorts?page =' +str(ShortsSpider.page_num)+'/'

    #     if ShortsSpider.page_num < ShortsSpider.max_page:
    #         ShortsSpider.page_num += 1

    #         yield response.follow(next_page,  callback=self.link_parse)


# color
# response.css(".swatch-group-selector.swatch-custom-image").css("::attr(orig-value)").extract()

             

