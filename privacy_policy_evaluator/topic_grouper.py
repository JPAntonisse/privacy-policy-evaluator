import os 
from os import listdir
from os.path import isfile, join

import TFIDF
import preprocessing

topics = ["location"]
threshold = 0.02

dirname = os.path.dirname(__file__)
paragraphs = open(dirname + "/data/policies/reddit.txt", "r", encoding="utf8").read()

# Preprocces the topics
topics = [preprocessing.lemmatization(topic) for topic in topics]
print(topics)

# compute corelation between words and paragraphs
TFIDF.calculate_vectors(paragraphs)


# Check configurable threshold

# Print related paragraphs

# merge paragrahs

# take rest

# Return dict of topic paragraphs