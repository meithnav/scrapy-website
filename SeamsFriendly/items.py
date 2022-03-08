# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# from turtle import title
import scrapy


class SeamsfriendlyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    ImgLinks = scrapy.Field()
    # colors = scrapy.Field()

