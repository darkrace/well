# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field
import scrapy
from scrapy.loader.processors import MapCompose, Join, TakeFirst, Identity
from w3lib.html import remove_tags
import re

# Processing Functions
def remove_quotations(field):
    return field.replace(u"\u201d", "").replace(u"\u201c", "")


def replace_newline_char(field):
    return field.replace(u"\n", " ").replace(u"\r", " ")


def strip_field(field):
    return field.strip()


def null_input(field):
    return None


def extract_digits(field):
    reference_regex = re.compile("\\d+")
    return reference_regex.findall(field)


def extract_currency_value(field):
    reference_regex = re.compile("[0-9]+(?:\.|,)[0-9]{0,2}")
    return [
        value.replace(u',', u'.') for value in reference_regex.findall(field)]

class WellItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class wellItems(Item):
    url = scrapy.Field()
    name = scrapy.Field(input_processor=MapCompose(remove_tags, strip_field))
    price = scrapy.Field(input_processor=MapCompose(remove_tags, strip_field))
    price_old = scrapy.Field(input_processor=MapCompose(remove_tags, strip_field))
    reference = scrapy.Field()
    image = scrapy.Field()
    description = scrapy.Field(
        input_processor=MapCompose(
            remove_tags, strip_field),
        output_processor=Identity(),
    )
    brand = scrapy.Field()
    brand_text = scrapy.Field()
    categories = scrapy.Field()
    availability = scrapy.Field()
    # sku = scrapy.Field()
    rating_average = scrapy.Field()
    rating_count = scrapy.Field()
    barcode = scrapy.Field()
    stock = scrapy.Field(input_processor=MapCompose(remove_tags, strip_field))
    timestamp = scrapy.Field()
    color = scrapy.Field()
    Material = scrapy.Field()
    Specification = scrapy.Field(input_processor=MapCompose(
        remove_tags,
        replace_newline_char,
        strip_field),output_processor=Identity() )
    image1 = scrapy.Field()
    image2 = scrapy.Field()
    image3 = scrapy.Field()
    image4 = scrapy.Field()
    image5 = scrapy.Field()
    image6 = scrapy.Field()
    image7 = scrapy.Field()
    image8 = scrapy.Field()
    image9 = scrapy.Field()
    image10 = scrapy.Field()
    image11 = scrapy.Field()
    image12 = scrapy.Field()
    image13 = scrapy.Field()
    image14 = scrapy.Field()
    image15 = scrapy.Field()