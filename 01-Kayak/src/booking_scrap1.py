import os
import logging
import pandas as pd

import scrapy
from scrapy.crawler import CrawlerProcess

from src.cities_weather import cities_meta_df
top_cities_weather_ls = cities_meta_df['cities_clean'].tolist()

# SCRAP1: Functions to scrap first four pages of hotels for different information

# Scrap first 25 hotels from page 1 (using offset)
class HotelBookingSpider(scrapy.Spider):
    # Name of your spider
    name = "HotelScraper"

    # Starting URL
    start_urls = ['https://www.booking.com/',]
    
    cities_ls = top_cities_weather_ls

    # Parse function for form request
    def parse(self, response):
        cities_ls = top_cities_weather_ls
        for i in range(len(cities_ls)):
            payload = {'ss':self.cities_ls[i],
            'checkin_year':'2022','checkin_month':'6','checkin_monthday':'4','checkout_year':'2022','checkout_month':'6','checkout_monthday':'10',
            'group_adults':'2','no_rooms':'1',
            'offset': '0'}
            yield scrapy.FormRequest.from_response(response, formdata = payload, callback = self.after_search)


    # Callback used after login
    def after_search(self, response):
        
        results = response.css('div.b978843432')
        
        
        for r in results:
            yield {
                'city': response.css('h1.e1f827110f.d3a14d00da::text').get().split(':')[0],
                'suburbs': r.css("span.f4bd0794db.b4273d69aa::text").get(),
                'hotel_name': r.css("div.fcab3ed991.a23c043802::text").get(),
                'link': r.css("a.e13098a59f::attr(href)").get(),
                'rating': r.css("div.b5cd09854e.d10a6220b4::text").get(),
                'room_type': r.css("span.df597226dd::text").get(),
                'price': r.css("span.fcab3ed991.bd73d13072::text").get(),
                'stay': r.css("div.d8eab2cf7f.dc2c6438ff::text").get().split(',')[0].strip(),
                'guests': r.css("div.d8eab2cf7f.dc2c6438ff::text").get().split(',')[1].strip(),
                'room':r.css("div.d8eab2cf7f::text").get(),
                'description': r.css("div.d506630cf3::text").get(),
                'location':r.css("span.cb5ebe3ffb span::text").get(),
                'map_link': r.css("a.fc63351294.a168c6f285.e0e11a8307.a25b1d9e47::attr(href)").get()
            }



# Scrap first 25 hotels from page 2 (using offset)
class HotelBookingSpiderp2(scrapy.Spider):
    # Name of your spider
    name = "HotelScraper"

    # Starting URL
    start_urls = ['https://www.booking.com/',]
    
    cities_ls = top_cities_weather_ls

    # Parse function for form request
    def parse(self, response):
        cities_ls = top_cities_weather_ls
        for i in range(len(cities_ls)):
            payload = {'ss':self.cities_ls[i],
            'checkin_year':'2022','checkin_month':'6','checkin_monthday':'4','checkout_year':'2022','checkout_month':'6','checkout_monthday':'10',
            'group_adults':'2','no_rooms':'1',
            'offset': '25'}
            yield scrapy.FormRequest.from_response(response, formdata = payload, callback = self.after_search)


    # Callback used after login
    def after_search(self, response):
        
        results = response.css('div.b978843432')
        
        
        for r in results:
            yield {
                'city': response.css('h1.e1f827110f.d3a14d00da::text').get().split(':')[0],
                'suburbs': r.css("span.f4bd0794db.b4273d69aa::text").get(),
                'hotel_name': r.css("div.fcab3ed991.a23c043802::text").get(),
                'link': r.css("a.e13098a59f::attr(href)").get(),
                'rating': r.css("div.b5cd09854e.d10a6220b4::text").get(),
                'room_type': r.css("span.df597226dd::text").get(),
                'price': r.css("span.fcab3ed991.bd73d13072::text").get(),
                'stay': r.css("div.d8eab2cf7f.dc2c6438ff::text").get().split(',')[0].strip(),
                'guests': r.css("div.d8eab2cf7f.dc2c6438ff::text").get().split(',')[1].strip(),
                'room':r.css("div.d8eab2cf7f::text").get(),
                'description': r.css("div.d506630cf3::text").get(),
                'location':r.css("span.cb5ebe3ffb span::text").get(),
                'map_link': r.css("a.fc63351294.a168c6f285.e0e11a8307.a25b1d9e47::attr(href)").get()
            }


# Scrap first 25 hotels from page 3 using offset
class HotelBookingSpiderp3(scrapy.Spider):
    # Name of your spider
    name = "HotelScraper"

    # Starting URL
    start_urls = ['https://www.booking.com/',]
    
    cities_ls = top_cities_weather_ls

    # Parse function for form request
    def parse(self, response):
        cities_ls = top_cities_weather_ls
        for i in range(len(cities_ls)):
            payload = {'ss':self.cities_ls[i],
            'checkin_year':'2022','checkin_month':'6','checkin_monthday':'4','checkout_year':'2022','checkout_month':'6','checkout_monthday':'10',
            'group_adults':'2','no_rooms':'1',
            'offset': '50'}
            yield scrapy.FormRequest.from_response(response, formdata = payload, callback = self.after_search)


    # Callback used after login
    def after_search(self, response):
        
        results = response.css('div.b978843432')
        
        
        for r in results:
            yield {
                'city': response.css('h1.e1f827110f.d3a14d00da::text').get().split(':')[0],
                'suburbs': r.css("span.f4bd0794db.b4273d69aa::text").get(),
                'hotel_name': r.css("div.fcab3ed991.a23c043802::text").get(),
                'link': r.css("a.e13098a59f::attr(href)").get(),
                'rating': r.css("div.b5cd09854e.d10a6220b4::text").get(),
                'room_type': r.css("span.df597226dd::text").get(),
                'price': r.css("span.fcab3ed991.bd73d13072::text").get(),
                'stay': r.css("div.d8eab2cf7f.dc2c6438ff::text").get().split(',')[0].strip(),
                'guests': r.css("div.d8eab2cf7f.dc2c6438ff::text").get().split(',')[1].strip(),
                'room':r.css("div.d8eab2cf7f::text").get(),
                'description': r.css("div.d506630cf3::text").get(),
                'location':r.css("span.cb5ebe3ffb span::text").get(),
                'map_link': r.css("a.fc63351294.a168c6f285.e0e11a8307.a25b1d9e47::attr(href)").get()
            }



# Scrap first 25 hotels from page 4 using offset
class HotelBookingSpiderp4(scrapy.Spider):
    # Name of your spider
    name = "HotelScraper"

    # Starting URL
    start_urls = ['https://www.booking.com/',]
    
    cities_ls = top_cities_weather_ls

    # Parse function for form request
    def parse(self, response):
        cities_ls = top_cities_weather_ls
        for i in range(len(cities_ls)):
            payload = {'ss':self.cities_ls[i],
            'checkin_year':'2022','checkin_month':'6','checkin_monthday':'4','checkout_year':'2022','checkout_month':'6','checkout_monthday':'10',
            'group_adults':'2','no_rooms':'1',
            'offset': '75'}
            yield scrapy.FormRequest.from_response(response, formdata = payload, callback = self.after_search)


    # Callback used after login
    def after_search(self, response):
        
        results = response.css('div.b978843432')
        
        
        for r in results:
            yield {
                'city': response.css('h1.e1f827110f.d3a14d00da::text').get().split(':')[0],
                'suburbs': r.css("span.f4bd0794db.b4273d69aa::text").get(),
                'hotel_name': r.css("div.fcab3ed991.a23c043802::text").get(),
                'link': r.css("a.e13098a59f::attr(href)").get(),
                'rating': r.css("div.b5cd09854e.d10a6220b4::text").get(),
                'room_type': r.css("span.df597226dd::text").get(),
                'price': r.css("span.fcab3ed991.bd73d13072::text").get(),
                'stay': r.css("div.d8eab2cf7f.dc2c6438ff::text").get().split(',')[0].strip(),
                'guests': r.css("div.d8eab2cf7f.dc2c6438ff::text").get().split(',')[1].strip(),
                'room':r.css("div.d8eab2cf7f::text").get(),
                'description': r.css("div.d506630cf3::text").get(),
                'location':r.css("span.cb5ebe3ffb span::text").get(),
                'map_link': r.css("a.fc63351294.a168c6f285.e0e11a8307.a25b1d9e47::attr(href)").get()
            }

# List of map links to be used for scrap2
scrap1_df = pd.read_csv('data/processed/scrap1_hotels_topcities_booking-clean.csv')
hotels_links_ls = scrap1_df["map_link"].tolist()