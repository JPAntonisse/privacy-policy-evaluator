from os import listdir
from os.path import isfile, join
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import collections


def split(text, delim=','):
    """
    Split a string into an array
    :param text:
    :param delim:
    :return:
    """
    return [x.strip() for x in text.split(delim)]


def read_file(file):
    """
    Reads a file and returns the text
    :param file:
    :return:
    """
    f = open(file, "r", encoding="utf8")
    return f.read()


def read_folder(folder):
    """
    Reads complete folder
    :param folder:
    :return:
    """
    file_names = [f for f in listdir(folder) if isfile(join(folder, f))]
    policies = []
    for file_name in file_names:
        f = open(folder + file_name, "r", encoding="utf8")
        policies.append(f.read())
    return policies


def calculate_vectors(text, ngram_min=1, ngram_max=1):
    ngram_range = (ngram_min, ngram_max)
    tfidf = TfidfVectorizer(ngram_range=ngram_range)
    vecs = tfidf.fit_transform(text)
    return [vecs, tfidf]


def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)

    return [w for w in word_tokens if not w in stop_words]


def most_common_words(array, common=10):
    # Pass the split_it list to instance of Counter class.
    Counter = collections.Counter(array)

    # most_common() produces k frequently encountered
    # input values and their respective counts.
    return Counter.most_common(common)
