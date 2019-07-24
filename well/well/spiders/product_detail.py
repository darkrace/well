# -*- coding: utf-8 -*-

import scrapy
from well.items import wellItems
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import urllib
import time
class ProductDetailSpider(scrapy.Spider):
    name = 'well'
    allowed_domains = ['kingsonsbags.com']
    # urls = [
    #     "AOC Curved 32 Inch Monitor - AG322QCX",
    #     "Asus 24 Inch WideScreen 3D capable Gaming Monitor [VG248QE]",
    #     "ASUS 27 Inch ROG Swift Gaming LED Monitor - PG279Q",
    #     "Asus AC86U Dual Band Wireless Gaming Router With Mu Mimo",
    #     "ASUS ROG PG278Q Black 27\" WQHD 2560 x 1440, 144 Hz 1ms(GTG) NVIDIA G - Sync Gaming Monitor with Exclusive GamePlus onscreen timer / crosshair, Tilt, Swivel, Pivot, Height Adjustable",
    #     "ASUS ROG Rapture GT-AC5300",
    #     "Asus ROG Swift PG258Q 24.5\" Full HD eSports Gaming Monitor",
    #     "ASUS RT-AC3200 Tri-Band Wireless Gigabit Router",
    #     "ASUS RT-AC5300 Wireless Tri-Band Gigabit Router",
    #     "ASUS RT-AC68U Wireless-AC1900 Dual-Band Gigabit Router",
    #     "Asus RT-AC87U Dual-band Wireless-AC2400 Gigabit Router, Red",
    #     "Asus RT-N12+ 3-in-1 Wireless Router/Access Point/Range Extender ",
    #     "Asus RT-N12HP High Power Wireless-N300 3-in-1 Router/AP/Range Extender",
    #     "ASUS VG278Q 27 inch Full HD 1080p 144Hz 1ms DP HDMI DVI Eye Care Gaming Monitor with FreeSync & Adaptive Sync",
    #     "CORSAIR MM300 Anti-Fray Cloth Gaming Mouse Pad - Designed for Maximum Control - Extended",
    #     "Corsair ST100 RGB Gaming Headset Stand",
    #     "Corsair STRAFE RGB Mechanical Cherry MX Red Gaming Keyboard",
    #     "D-Link AC5300 Ultra Wi-Fi HD Streaming and Gaming Router, Red - DIR-895L",
    #     "HP Color LaserJet Pro MFP M377dw",
    #     "Hp Laserjet Printer Pro M102A",
    #     "HP LaserJet Pro M227fdw All-in-One Wireless Laser Printer",
    #     "HP LaserJet Pro MFP M130fw(G3Q60A)",
    #     "HP LaserJet Pro MFP M227fdw Multifunction Printer - G3Q75A",
    #     "HyperX Alloy FPS Mechanical Gaming Keyboard, Cherry MX Blue, Red LED (HX-KB1BL1-NA/A2",
    #     "HyperX Cloud Alpha Pro Gaming Headset for PC, PS4 & Xbox One, Nintendo Switch (HX-HSCA-RD/EE)",
    #     "HyperX Cloud Headset Gaming Headphones with Mic for Nintendo Switch and Mobile Gaming (HX-HSCEB-RD)",
    #     "HyperX Cloud II Gaming Headset for PC & PS4 - Gun Metal",
    #     "HyperX Cloud II Gaming Headset KHX-HSCP-RD - Red",
    #     "HyperX Cloud Revolver Gaming Headset , Black , HX-HSCRS-GM/EE",
    #     "HyperX Cloud Revolver S Gaming Headset with Dolby 7.1 Surround Sound HX-HSCRS-GM/EE",
    #     "HyperX Cloud Stinger core Gaming Headset",
    #     "HyperX Cloud Stinger Gaming Headset",
    #     "Hyperx Cloud Stinger Wireless USB Wireless Gaming Headset for PS4 - HX-HSCSW-BK",
    #     "HyperX Fury S Pro Gaming Mouse Pad Small HX-MPFS-SM Large HX-MPFS-L",
    #     "HyperX Pulsefire FPS Gaming Mouse & HyperX FURY S Medium Mouse Pad Bundle - HXK-DM01",
    #     "Kingston 240GB SSD SA400 Sata3 2.5"" -  SA400S37/240G",
    #     "LG  DVD-RW External Drive 8X USB 2.0 Super Multi Ultra Slim Portable Retail (Black) GP65NB60",
    #     "LG 22-inch Full HD IPS LED Monitor with AMD Free Sync -22MK430H",
    #     "LG 24 inch Full HD IPS LED Monitor with AMD FreeSync -24MK430H",
    #     "LG 24MP88HV-S IPS Monitor with Infinity Display - 24-Inch",
    #     "LG 34 Inch Curved UltraWide LED Monitor - 34UC98",
    #     "LG 34 Inch UltraWide Curved Gaming LED Monitor - 34UC79G",
    #     "Linksys E900 Wireless-N300 Wi-Fi Router With 4-Port Switch, Black",
    #     "Linksys EA6350 AC1200+ Dual-Band Smart Wi-Fi Wireless Router, Black",
    #     "Linksys EA6900 AC1900 Dual Band Router, Black",
    #     "Linksys EA9500 Max-Stream AC5400 MU-MIMO Gigabit Router, Black",
    #     "Linksys LAPAC1750pro Business AC1750 Pro Dual-band Access Point, White",
    #     "LINKSYS LAPAC2600 BUSINESS PRO SERIES WIRELESS-AC DUAL-BAND MU-MIMO ACCESS POINT",
    #     "LINKSYS LAPN300 BUSINESS ACCESS POINT WIRELESS WI-FI SINGLE BAND 2.4GHZ N300 WITH POE",
    #     "LINKSYS LAPN600 BUSINESS ACCESS POINT WIRELESS WI-FI DUAL BAND 2.4   5GHZ N600 WITH POE",
    #     "Linksys RE6400-ME AC1200 Dual Band Wireless Range Extender",
    #     "Linksys WHW0303 Velop Whole Home Mesh Wi-Fi System Router, White, Pack Of 3",
    #     "Logitech Craft Wireless US Keyboard with Creative Input Dial - Black",
    #     "Logitech H151 Stereo Headset - Black",
    #     "Logitech M185 Wireless Mouse",
    #     "Logitech M185 Wireless Mouse, Swift Gray",
    #     "Logitech M90 910-001794 Mouse",
    #     "Logitech M90 Optical Wired Mouse - Black",
    #     "Logitech MK220 Wireless Combo En-AR Keyboard and Mouse - Black",
    #     "Logitech MK235 Wireless Keyboard and Mouse - Black",
    #     "Logitech MK710 Wireless Desktop Keyboard and Mouse [English/Arab]",
    #     "Logitech Wireless Combo for PC - MK235 ",
    #     "Logitech Wireless Combo MK220",
    #     "Logitech Wireless Combo Mk220 With Keyboard And Mouse .",
    #     "Logitech Wireless Mk220 Keyboard And Mouse Combo (black)",
    #     "MSI Curved 24 Inch Monitor - OPTIX MAG24C",
    #     "MSI Curved 27 Inch Monitor - OPTIX-MPG27C",
    #     "MSI Optix AG32C Full HD FreeSync 32 inch Curved Gaming Monitor",
    #     "MSI Optix MAG27C Curved 27 inch Gaming Monitor",
    #     "PenPower WorldCard Color Scanner [PT-WCOECL]",
    #     "RANGE EXTENDER TP LINK AC750 Wi-Fi RE200",
    #     "Samsung 22 inch LED Monitor - LS22F350FHMXZN",
    #     "Samsung 28 inch 4K UHD LED Monitor - LU28E590DS",
    #     "Samsung 32 inch LCD Monitor - C32F391FWM",
    #     "SAMSUNG 34 inch Curved USB C type Business series display ( 890 Series )",
    #     "Samsung 49 Inch QLED Gaming Monitor with Super Ultra-Wide Screen - LC49HG90DMM",
    #     "Samsung LED 24 Inch Monitor - 24F350FH",
    #     "Screen Gaming Monitor Curved QHD 34 Inch by Asus , PG348Q",
    #     "Seagate 1 TB Backup Plus USB 3.0 Slim Portable Hard Drive - Black [STDR1000200]",
    #     "Seagate 1 TB Backup Plus USB 3.0 Slim Portable Hard Drive - Black [STDR1000200]",
    #     "Seagate 2 TB Backup Plus USB 3.0 Slim Portable Hard Drive - Black [STDR2000200]",
    #     "Seagate Backup Plus 4TB Portable USB 3.0 Hard Drive STDR4000200 - Black",
    #     "Stereo Gaming Headphone USB Multimedia Gaming With Microphone Opal SF-GH400 For Notebook Computer Black Color",
    #     "TP-Link RE200 AC750 Wi-Fi router Range Extender",
    #     # "WD 2TB My Passport  Portable External Hard Drive USB 3.0 - Black, WDBYFT0020BBK",
    #
    # ]
    start_urls=[
        "https://web.archive.org/web/20190703075054/https://www.kingsonsbags.com/product-category/shoulder-bags/",
        "https://web.archive.org/web/20190703075054/https://www.kingsonsbags.com/product-category/tablet-shoulder-bags/",
        "https://web.archive.org/web/20190703075054/https://www.kingsonsbags.com/product-category/backpacks/",
        "https://web.archive.org/web/20190703075054/https://www.kingsonsbags.com/product-category/laptop-sleeves/",
        "https://web.archive.org/web/20190703075054/https://www.kingsonsbags.com/product-category/trolley-bags/",
        "https://web.archive.org/web/20190703075054/https://www.kingsonsbags.com/product-category/hard-drive-cases/",
    ]
    # for url in  urls:
    #     start_urls.append("https://www.amazon.ae/s?k="+urllib.parse.quote_plus(url))

    i =1
    def parse(self, response):

        for sel in response.xpath("//ul[@class='products']/li//img/parent::a/@href").getall():
            #     item = ProductionItem()
            #     item['listurl'] = sel.xpath('//a[@id="link101"]/@href').extract()[0]
            #


            request = scrapy.Request(sel, callback=self.parse_items)
            request.meta['proxy'] = "208.98.185.89:53630"
            yield request
    # def parse_page(self,response):
    #     pass
    def parse_items(self, response):
        Categories, comment_list, descrip, review, user = [], [], [], {}, []
        item = wellItems()

        item['Title'] = response.xpath("//h1[@class='product_title entry-title']/text()").get().strip()
        item['OldPrice'] = response.xpath("//span[@class='priceBlockStrikePriceString a-text-strike']/text()").get()
        item['CurrentPrice'] = response.xpath("//span[@id='priceblock_ourprice']/text()").get()
        # item['Stock'] = response.xpath("//div[@id='gtm-main-product-page']//span[@id='stock_amount2']/text()").get()
        item['Image'] = response.xpath("//div[@id='imgTagWrapperId']/img/@src").get()
        item['Url'] = response.url
        item['Availability'] = response.xpath("//div[@id='availability']/span/text()").get()
        item['Rating_value'] = response.xpath("//a[@class='a-popover-trigger a-declarative']/i/span/text()").get()
        # item['Rating_max'] = '5'
        # item['Sku'] = response.xpath("substring-before(substring-after(//div[@class='container distr-main-block']//div[contains(@class,'single-product-desc')]/p/text(),'SKU: '),'|')").get()


        # user.append(response.xpath("//span[@class='product_text product_text_review']/text()").getall())
        # comment_list.append(response.xpath("//p[@class='product_text product_text_product_subtitle product_review_list_paragraph']/text()").getall())
        # descrip.append(response.xpath("//div[@id='productDescription']//p//text()").get())
        descrip.append(response.xpath("//div[@id='productDescription']//p//text()").getall())

        item['Description'] = descrip
        # review['user'] = user
        # review['comment'] = comment_list
        # item['Reviews'] = review

        # item['Description'] = descrip
        # item['Barcode'] = response.xpath("substring-after(//div[@class='container distr-main-block']//div[contains(@class,'single-product-desc')]/p/text(),'Barcode: ')").getall()
        item['Brand'] = response.xpath("//div[@id='bylineInfo_feature_div']/div/a[@id='bylineInfo']/text()").get()

        # import pandas as pd
        # # csvinputlist = ['/home/dark/TA/well/oskarphone.csv']
        # # csvinput = csvinputlist
        #  # continue for as many column that are in the file
        # df = pd.read_csv('/home/dark/TA/well/oskarphone.csv')
        # headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        # df.loc[self.i, "Title"] = response.xpath("//h5[@class='top-title']/text()").get().strip()
        # # df['Stock'][self.i] = response.xpath("//div[@id='gtm-main-product-page']//span[@id='stock_amount2']/text()").get()
        # df.loc[self.i, "Image"]= response.xpath("//div[@class='preview-pic tab-content']/div[@id='pic-1-0']/img/@src").get()
        # df.loc[self.i, "Barcode"] = response.xpath("substring-after(//div[@class='container distr-main-block']//div[contains(@class,'single-product-desc')]/p/text(),'Barcode: ')").get()
        # df.loc[self.i, "Description"] = str(descrip[0])
        # df.loc[self.i, "Brand"] = response.xpath("substring-before(//div[@class='container distr-main-block']//div[contains(@class,'single-product-desc')]/p/text(),'|')").get()
        # df.loc[self.i, "URL"] = response.url
        # print(self.i)
        # df.to_csv('/home/dark/TA/well/oskarphone.csv')
        # time.sleep(2)
        self.i+=1
        print(self.i)
        yield item