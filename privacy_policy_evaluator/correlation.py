
import nltk
from nltk.tokenize import word_tokenize
from nltk.text import Text

from sklearn.feature_extraction.text import CountVectorizer
import re

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
import TFIDF
import string
import os
from os import listdir
from os.path import isfile, join

dirname = os.path.dirname(__file__)

def correlation_matrix(relative_folder_path, verbose=0, ngram_min = 1, ngram_max = 1):

    files_path = os.path.join(dirname, relative_folder_path)

    policies_file_names = [f for f in listdir(files_path) if isfile(join(files_path, f) )]
    policy_company_names = [name.split('.')[0] for name in policies_file_names] 

    # Select a policy text
    policies = []
    for file_name in policies_file_names:
        f = open(files_path + file_name, "r", encoding="utf8")
        policies.append(f.read())

        ##https://kavita-ganesan.com/extracting-keywords-from-text-tfidf/

    def sort_coo(coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)
    
    def extract_topn_from_vector(feature_names, sorted_items, topn=10):
        """get the feature names and tf-idf score of top n items"""
        
        #use only topn items from vector
        sorted_items = sorted_items[:topn]
    
        score_vals = []
        feature_vals = []
        
        # word index and corresponding tf-idf score
        for idx, score in sorted_items:
            
            #keep track of feature name and its corresponding score
            score_vals.append(round(score, 3))
            feature_vals.append(feature_names[idx])
    
        #create a tuples of feature,score
        #results = zip(feature_vals,score_vals)
        results= {}
        for idx in range(len(feature_vals)):
            results[feature_vals[idx]]=score_vals[idx]
        
        return results

    if verbose > 0 :
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")
        print(f"Correlation matrix with n-gram size({ngram_min}, {ngram_max})")
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")

    vecs = TFIDF.calculate_vectors(policies, ngram_min=ngram_min, ngram_max = ngram_max)

    corr_matrix = ((vecs * vecs.T).A)
    df = pd.DataFrame(corr_matrix, columns = policy_company_names)
    df.insert(0, "document", policy_company_names, True) 
    
    if verbose > 0:
        print_correlation_matrix(df)
        feature_names = tfidf.get_feature_names()
        n_features = 5 
        print("#######")
        print(" Top features:")
        print()

        #sort the tf-idf vectors by descending order of scores
        sorted_items=sort_coo(vecs.tocoo())

        #extract only the top n; n here is 10
        keywords=extract_topn_from_vector(feature_names,sorted_items,10)

        for k in keywords:
            print(k,keywords[k])

        print()
        print("#######")
        print()

    return df

def print_correlation_matrix(dataframe):
    print(dataframe.to_string(index=False))

files_path = "data/policies/"

df = correlation_matrix(files_path, verbose=0, ngram_min = 1, ngram_max = 2)
print_correlation_matrix(df) 