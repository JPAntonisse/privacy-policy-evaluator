import os 
from os import listdir
from os.path import isfile, join

import numpy as np

import TFIDF
import preprocessing
import paragraphing

topics = ["location", "kaas"]
threshold = 0.02

#Example

dirname = os.path.dirname(__file__)
policy = open(dirname + "/data/policies/reddit.txt", "r", encoding="utf8").read()

paragraphs = paragraphing.paragraphing(policy)[0]
preprocessed_paragraphs = preprocessing.full_preproccessing( paragraphs, ["reddit.inc", "reddit.inc"])

# Preprocces the topics
topics = [preprocessing.lemmatization(topic) for topic in topics]
print(topics)

# compute corelation between words and paragraphs
[vecs, tfidf] = TFIDF.calculate_vectors(paragraphs + topics)
# result = tfidf.transform(topics)
# # print(result)
scores = (vecs[0, :] * vecs[1:, :].T).A[0]

feature_names = tfidf.get_feature_names()
topic_feature_indices = []
for i in range(len(topics)):
    feature_index = vecs[-(i + 1), :].indices[0]
    topic_feature_indices.append(feature_index)

# Find matches
scores = []
for i in range(0, len(paragraphs)):
    for index in topic_feature_indices:
        score = vecs[i, index][0, 0]
        print(score)



print('aaaa')
print()
best_score = np.argmax(scores)
print(best_score)
answer = paragraphs[best_score]
print(paragraphs[0])

# 0.30864921589522937

# Check configurable threshold

# Print related paragraphs

# merge paragrahs

# take rest

# Return dict of topic paragraphs