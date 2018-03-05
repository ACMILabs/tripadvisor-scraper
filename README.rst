TripAdvisor Scraper
-------------------

This is a Python3 Scrapy configuration that gets ACMI's reviews from tripadvisor.

To use, install requirements, then run something like::

    scrapy runspider tripadvisorscraper.py -o reviews.csv

TODO
====

- Make it scrape the full reviews rather than just the summaries (this involves following any 'More' links - or all
links to individual reviews)