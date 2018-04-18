#!/usr/bin/env python3
import logging
import json
import os
import glob

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

input_dir = "json/"

logger.info("Start")
input_files = glob.glob(input_dir + "*.json")
authors_and_revid = []
by_author = {}
for f_name in input_files:
	f = open(f_name, 'r')
	reviews = json.load(f)['Reviews']
	for review in reviews:
		by_author.setdefault(review['Author'], []).append(review['ReviewID'])

nb_rev_by_author = {}
for author, reviews in by_author.items():
	nb_rev_by_author[author] = len(reviews)

assert min(nb_rev_by_author.values()) >= 1
highest_freq = max(nb_rev_by_author.values())

freq_by_nb_rev = {}
for author, nb_rev in nb_rev_by_author.items():
	freq_by_nb_rev[nb_rev] = freq_by_nb_rev.get(nb_rev, 0) + 1

assert highest_freq in freq_by_nb_rev

freq_cumul_by_nb_rev = {}
summ = 0
for nb_rev, freq in sorted(freq_by_nb_rev.items(), reverse=True):
	summ += freq
	freq_cumul_by_nb_rev[("≥", nb_rev)] = summ

for nb_rev, freq_cumul in sorted(freq_cumul_by_nb_rev.items()):
	print("≥" + str(nb_rev[1]) + ": " + str(freq_cumul))

# TODO: compute, for each hotel, for each criterion: average grade

