# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class WellItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class wellItems(Item):
    Url             = Field()
    Title           = Field()
    # Sku        = Field()
    CurrentPrice    = Field()
    OldPrice    = Field()
    Image           = Field()
    Description     = Field()
    Availability    = Field()
    # Stock           = Field()
    Rating_value    = Field()
    # Rating_max      = Field()
    # ReviewCount     = Field()
    # Reviews         = Field()
    # Categories      = Field()
    Brand           = Field()
    # Barcode           = Field()


