from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import os

dirname = os.path.dirname(__file__)


def correlation_matrix(policies, company_name=None, verbose=0, ngram_min=1, ngram_max=1):
    """
    Makes the correlation matrix from different policies in array policies[]
    :param company_name:
    :param policies:
    :param verbose:
    :param ngram_min:
    :param ngram_max:
    :return:
    """

    #     ##https://kavita-ganesan.com/extracting-keywords-from-text-tfidf/
    def sort_coo(coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

    def extract_topn_from_vector(feature_names, sorted_items, topn=10):
        """get the feature names and tf-idf score of top n items"""
        # use only topn items from vector
        sorted_items = sorted_items[:topn]

        score_vals = []
        feature_vals = []

        # word index and corresponding tf-idf score
        for idx, score in sorted_items:
            # keep track of feature name and its corresponding score
            score_vals.append(round(score, 3))
            feature_vals.append(feature_names[idx])
        # create a tuples of feature,score
        # results = zip(feature_vals,score_vals)
        results = {}
        for idx in range(len(feature_vals)):
            results[feature_vals[idx]] = score_vals[idx]

        return results

    if verbose > 0:
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")
        print(f"Correlation matrix with n-gram size({ngram_min}, {ngram_max})")
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")

    ngram_range = (ngram_min, ngram_max)
    tfidf = TfidfVectorizer(ngram_range=ngram_range)
    vecs = tfidf.fit_transform(policies)

    corr_matrix = (vecs * vecs.T).A
    df = pd.DataFrame(corr_matrix, columns=company_name)
    df.insert(0, "document", company_name, True)

    if verbose > 0:
        print_correlation_matrix(df)
        feature_names = tfidf.get_feature_names()
        n_features = 5
        print("#######")
        print(" Top features:")
        print()

        # sort the tf-idf vectors by descending order of scores
        sorted_items = sort_coo(vecs.tocoo())

        # extract only the top n; n here is 10
        keywords = extract_topn_from_vector(feature_names, sorted_items, 10)

        for k in keywords:
            print(k, keywords[k])
        print()
        print("#######")
        print()

    return df


def print_correlation_matrix(dataframe):
    print(dataframe.to_string(index=False))
