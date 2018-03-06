TripAdvisor Scraper
-------------------

This is a Python3 Scrapy configuration that gets ACMI's reviews from tripadvisor.

To use, run ``pip install -r requirements.txt``, then something like::

    scrapy runspider tripadvisorscraper.py -o reviews.csv

This will generate a CSV file of your reviews. You could load the CSV into
Excel and sort by rating, then copy/paste the text for each rating into your
favourite text analysis tool.

Some simple topic analysis can be seen with::

    python3 ./analyse_csv.py reviews.csv

This produces ranked lists of topics for each rating, showing the most relevant
topics found in the text of the reviews for each rating.

TODO
====

- Make it scrape the full reviews rather than just the summaries (this involves following any 'More' links - or all
  links to individual reviews).