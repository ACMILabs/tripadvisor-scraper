#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import scrapy



# TA uses javascript for the next/prev page controls, which are nontrivial to
# scrape. Lucklily the URLs are predictable, so we'll just generate them.
# TODO: get the number of pages from the initial scrape?
URL_TEMPLATE = 'https://www.tripadvisor.com.au/Attraction_Review-g255100-d269501-Reviews-or%s-Australian_Centre_for_the_Moving_Image-Melbourne_Victoria.html'
NUM_PAGES = 116
def url_generator():
    for page in range(NUM_PAGES):
        yield URL_TEMPLATE % (page * 10)


class TripAdvisorReview(scrapy.Spider):
    name = "tripadvisor"
    start_urls = list(url_generator())

    def parse(self, response):
        for review in response.css('.reviewSelector'):
            id = review.css('::attr(id)').extract_first()
            if id.startswith("review_title"):
                continue

            yield {
                'id': id.replace("review_", ""),
                'title': review.css('.quote ::text').extract_first(),
                'body': review.css('.partial_entry ::text').extract_first(),
                'rating': int(review.css('.rating   .ui_bubble_rating ::attr(class)').re(r'ui_bubble_rating bubble_(\d\d)')[0])/10.0,
            }


