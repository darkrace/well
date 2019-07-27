# -*- coding: utf-8 -*-

import scrapy
from well.items import wellItems
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import urllib
import time
import os
import json
from io import StringIO
import pkgutil
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from scrapy.loader import ItemLoader
from scrapy.exceptions import CloseSpider
import re
from lxml import etree
from collections import defaultdict

class ProductDetailSpider(scrapy.Spider):
    name = 'well'

    def __init__(self, config=None, *args, **kwargs):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
        self.chrome_options.add_argument("--headless")
        self.htmlparser = etree.HTMLParser()
        self.chrome_options.binary_location = '/opt/google/chrome/google-chrome'
        self.driver = webdriver.Chrome(
            executable_path=os.path.abspath("/home/dark/Downloads/chromedriver_linux64/chromedriver"),
            chrome_options=self.chrome_options)
        if config is not None:
            try:
                data = pkgutil.get_data("well", config)
                print("Data obtained from config: ", data)
                self.json_config = json.loads(data)
                self.count = 0
            except IOError as FileNotFoundException:
                print("File not found.")
                raise CloseSpider(reason=FileNotFoundException)

            if self.json_config is not None:
                self.start_urls = self.json_config['start_urls']
                self.selectors = self.json_config['fields']
                # self.rules = (
                #     # Detail Item Link Extraction Rule
                #     Rule(
                #         link_extractor=LinkExtractor(
                #             restrict_xpaths=self.json_config['links']['detail']),
                #         callback='parse_item',
                #         follow=False
                #     ),
                #     # Next Page Link Extraction Rule
                #     Rule(
                #         link_extractor=LinkExtractor(
                #             tags=('a', 'link', 'area'),
                #             restrict_xpaths=self.json_config['links']['next_page']),
                #         callback=None,
                #         follow=True
                #     )
                # )
            else:
                raise CloseSpider(
                    reason="Json config file has NoneType. Closing spider..."
                )
            super().__init__(*args, **kwargs)
        else:
            raise CloseSpider("Configuration argument was not specified!")

    i =1

    def parse(self, response):

        # for a in search("https://www.fragrantica.com/perfume/Dolce-Gabbana/Light-Blue-485.html", tld="co.in", num=1, stop=1, pause=2):
        #     print(a)

        self.driver.get(response.url)
        delay = 5  # seconds
        try:
            myElem = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'grid-view-item__link')))
            fields = StringIO(self.driver.page_source)
            tree = etree.parse(fields, self.htmlparser)
            for sel in tree.xpath(self.json_config['links']['detail']):

                request = scrapy.Request("https://uk.targus.com"+sel, callback=self.parse_items)
                # request.meta['proxy'] = "138.197.108.5:3128"
                yield request
            for sel in tree.xpath(self.json_config['links']['next_page']):
                request = scrapy.Request(sel, callback=None)
                # request.meta['proxy'] = "3.212.104.192:80"
                yield request
            print("Page is ready!")
        except TimeoutException:

            print("Loading took too much time!")

        # for sel in myElem.xpath("//ul[@class='products']/li//img/parent::a/@href").getall():
        #     #     item = ProductionItem()
        #     #     item['listurl'] = sel.xpath('//a[@id="link101"]/@href').extract()[0]
        #     #
        #
        #
        #     request = scrapy.Request(sel, callback=self.parse_items)
        #     request.meta['proxy'] = "208.98.185.89:53630"
        #     yield request
    # def parse_page(self,response):
    #     pass
    def parse_items(self, response):
        self.driver.get(response.url)
        item = wellItems()
        delay = 5
        try:
            myElem = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'pdp-spec-label')))
            fields = StringIO(self.driver.page_source)
            tree = etree.parse(fields, self.htmlparser)

            for key, value in self.selectors.items():
                if value:
                    item[key] = tree.xpath(value)
                    item['url'] = response.url

        except:
            pass
            # Categories, comment_list, descrip, review, user = [], [], [], {}, []
            # item = wellItems()
            # for key, value in self.selectors.items():
            #     item[key] = tree.xpath(value).get()
            # item['OldPrice'] = tree.xpath("//span[@class='priceBlockStrikePriceString a-text-strike']/text()").get()
            # item['CurrentPrice'] = tree.xpath("//span[@id='priceblock_ourprice']/text()").get()
            # # item['Stock'] = tree.xpath("//div[@id='gtm-main-product-page']//span[@id='stock_amount2']/text()").get()
            # item['Image'] = tree.xpath("//div[@id='imgTagWrapperId']/img/@src").get()
            # item['Url'] = tree.url
            # item['Availability'] = tree.xpath("//div[@id='availability']/span/text()").get()
            # item['Rating_value'] = tree.xpath("//a[@class='a-popover-trigger a-declarative']/i/span/text()").get()
            # # item['Rating_max'] = '5'
            # # item['Sku'] = tree.xpath("substring-before(substring-after(//div[@class='container distr-main-block']//div[contains(@class,'single-product-desc')]/p/text(),'SKU: '),'|')").get()
            #
            #
            # # user.append(tree.xpath("//span[@class='product_text product_text_review']/text()").getall())
            # # comment_list.append(tree.xpath("//p[@class='product_text product_text_product_subtitle product_review_list_paragraph']/text()").getall())
            # # descrip.append(tree.xpath("//div[@id='productDescription']//p//text()").get())
            # descrip.append(tree.xpath("//div[@id='productDescription']//p//text()").getall())
            #
            # item['Description'] = descrip
            # # review['user'] = user
            # # review['comment'] = comment_list
            # # item['Reviews'] = review
            #
            # # item['Description'] = descrip
            # # item['Barcode'] = tree.xpath("substring-after(//div[@class='container distr-main-block']//div[contains(@class,'single-product-desc')]/p/text(),'Barcode: ')").getall()
            # item['Brand'] = tree.xpath("//div[@id='bylineInfo_feature_div']/div/a[@id='bylineInfo']/text()").get()


        self.i+=1
        print(self.i)
        yield item

        # loader = ItemLoader(item=wellItems(), response=response)
        # loader.add_value('url', response.url)
        # for key, value in self.selectors.items():
        #     if value:
        #         loader.add_xpath(key, value)
        #         try:
        #             if self.json_config['regex'][key]:
        #                 regex_xpath = self.json_config['regex'][key]
        #                 loader._values[key][0] = re.search(regex_xpath[0], response.xpath(value).get()).group(
        #                     regex_xpath[1]).strip()
        #         except:
        #             try:
        #                 if self.json_config['regex'][key]:
        #                     loader._values[key][0] = ''
        #             except:
        #                 pass
        # self.count += 1
        # # loader.add_value('timestamp', int(time.time()))
        # item = loader.load_item()
        # for key, value in self.selectors.items():
        #     if (item.get(key) is None):
        #         print("[Warning] key: {0} is null!".format(key))
        # print("\n\n\n\n", self.count)
        # return item

