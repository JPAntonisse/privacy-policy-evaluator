from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_vectors(text, ngram_min = 1, ngram_max = 1):
    ngram_range = (ngram_min, ngram_max)
    tfidf = TfidfVectorizer(ngram_range= ngram_range)
    vecs = tfidf.fit_transform(text)
    return [vecs, tfidf]