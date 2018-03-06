#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from pprint import pprint

from topic_extraction import score_keyphrases_by_textrank
import sys
from collections import defaultdict


def main(csv_file):
    # load CSV
    # create corpus of text for each rank
    # extract terms for each rank
    corpus = defaultdict(str)

    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = reader.__next__()
        for row in reader:
            row_data = dict(zip(header, row))
            corpus[row_data['rating']] += row_data['title'] + " " + row_data['body']

    analysis = {}
    for k, v in corpus.items():
        analysis[int(float(k))] = score_keyphrases_by_textrank(v)

    pprint(analysis)



if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    args = parser.parse_args()
    main(args.csv_file)