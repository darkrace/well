import scrapy
from scrapy.cmdline import execute
# Just to run on pycharm
# execute(['scrapy', 'crawl','well'])
execute(['scrapy', 'crawl', 'well','-a','config=config/targus.json','-o','output.csv'])