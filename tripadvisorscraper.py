#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import scrapy


NUM_PAGES = 116


def url_generators():
    for page in range(NUM_PAGES):
        yield 'https://www.tripadvisor.com.au/Attraction_Review-g255100-d269501-Reviews-or%s-Australian_Centre_for_the_Moving_Image-Melbourne_Victoria.html' % (page * 10)


URLS = list(url_generators())

class TripAdvisorReview(scrapy.Spider):
    name = "tripadvisor"
    start_urls = URLS

    def parse(self, response):
        for review in response.css('.reviewSelector'):
            id = review.css('::attr(id)').extract_first()
            if id.startswith("review_title"):
                continue

            # import pdb; pdb.set_trace()

            yield {
                'id': id.replace("review_", ""),
                'url': response.request.url,
                'title': review.css('.quote ::text').extract_first(),
                'body': review.css('.partial_entry ::text').extract_first(),
                'rating': int(review.css('.rating   .ui_bubble_rating ::attr(class)').re(r'ui_bubble_rating bubble_(\d\d)')[0])/10.0,
            }


        # for href in response.xpath('//div[@class="property_title"]/a/@href').extract():
        #     url = response.urljoin(href)
        #     if url not in urls:
        #         urls.append(url)
        #
        #         yield scrapy.Request(url, callback=self.parse_page)

    #     for review_page in response.xpath('//div[@class="wrap"]/div/a/@href'):
    #         url = response.urljoin(review_page[i])
    #         yield scrapy.Request(url, self.parse_review)
    #
    #     review_page = response.xpath('//div[@class="wrap"]/div/a/@href').extract()
    #     if review_page:
    #         for i in range(len(review_page)):
    #             url = response.urljoin(review_page[i])
    #             yield scrapy.Request(url, self.parse_review)
    #
    #
    #     next_page = response.xpath('//div[@class="unified pagination "]/a/@href').extract()
    #     if next_page:
    #         url = response.urljoin(next_page[-1])
    #         print(url)
    #         yield scrapy.Request(url, self.parse)
    #
    # def parse_page(self, response):
    #
    #     review_page = response.xpath('//div[@class="wrap"]/div/a/@href').extract()
    #
    #     if review_page:
    #         for i in range(len(review_page)):
    #             url = response.urljoin(review_page[i])
    #             yield scrapy.Request(url, self.parse_review)
    #
    #     next_page = response.xpath('//div[@class="unified pagination "]/a/@href').extract()
    #     if next_page:
    #         url = response.urljoin(next_page[-1])
    #         yield scrapy.Request(url, self.parse_page)
    #
    #
    # def parse_review(self, response):
    #     item = ReviewItem()
    #
    #     contents = response.xpath('//div[@class="entry"]/p').extract()
    #     content = contents[0].encode("utf-8")
    #
    #     ratings = response.xpath('//span[@class="rate sprite-rating_s rating_s"]/img/@alt').extract()
    #     rating = ratings[0][0]
    #
    #
    #     item['rating'] = rating
    #     item['review'] = content
    #     yield item