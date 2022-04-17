import os
import logging
import pandas as pd

import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup

from src.booking_scrap1 import hotels_links_ls

# SCRAP2: Functions to scrap latitude and longitude of hotels using map link obtained from scrap1 (hotel_liks_ls)

class HotelLatLonSpider(scrapy.Spider):
    name = "hotel_latlon"

    start_urls = hotels_links_ls

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u,callback=self.parse)

    def parse(self, response):
        # use lxml to get decent HTML parsing speed
        soup = BeautifulSoup(response.text, 'lxml')

        result = soup.find('a', {'id':'hotel_address','class': 'jq_tooltip loc_block_link_underline_fix bui-link show_on_map_hp_link show_map_hp_link'})
        
        
        yield {
            "hotel_name" : result['title'].split(',')[0].replace('\\', ''),
            "hotel_lat" : result['data-atlas-latlng'].split(',')[0],
            "hotel_lon" : result['data-atlas-latlng'].split(',')[1]
            
        }
