# -*- coding: utf-8 -*-
import scrapy
import datetime

class HRForecastSpider(scrapy.Spider):
    name = 'hrforecast'
    allowed_domains = ['hrforecast.de']
    start_urls = ['http://www.hrforecast.de/career/']

    def parse(self, response):
        # follow vacancy's links
        for href in response.css('.entry-title a::attr(href)'):
            yield response.follow(href, self.parse_job)


    def parse_job(self, response):
        yield {
        'job_title': response.xpath('//div[@class="avia_textblock  "]/p/strong/text()').extract_first(),
        'company_name': 'HRForecast',
        'crawled_date': datetime.datetime.utcnow().strftime('%Y-%m-%d'),
        'posted_date': '',
        'job_description': response.xpath('//div[@class="avia_textblock  "]/p').extract(),
        'job_url': response.url
        }



