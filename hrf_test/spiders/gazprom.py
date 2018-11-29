# -*- coding: utf-8 -*-
import scrapy
import datetime

class HRForecastSpider(scrapy.Spider):
    name = 'gazprom'
    allowed_domains = ['gazpromvacancy.ru']
    start_urls = ['https://www.gazpromvacancy.ru/jobs/']

    def parse(self, response):
        # follow vacancy's links
        for href in response.css('.job-list-item a::attr(href)'):
            yield response.follow(href, self.parse_job)

        # follow pagination links
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)


    def parse_job(self, response):
        yield {
        'job_title': response.css('.job-title::text').extract_first(),
        'company_name': response.xpath('//dl[@class="job-params inline"]/dd[1]/a/text()').extract_first(),
        'crawled_date': datetime.datetime.utcnow().strftime('%Y-%m-%d'),
        'posted_date': response.xpath('//dl[@class="job-params inline"]/dd[5]/time/@datetime').extract_first(),
        'job_description': response.xpath('//div[@class="job-info plain"]').extract(),
        'job_url': response.url
        }