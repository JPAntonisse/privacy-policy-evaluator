import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from privacy_policy_evaluator import helpers, wordscoring, preprocessing, correlation

# Comparison Twitter reddit, correlation matrix
def compare_twitter_reddit_correlation(ngram_min, ngram_max):
    dir_name = os.path.dirname(os.path.realpath(__file__))
    folder_dir = "/../privacy_policy_evaluator/data/policies/"
    path = dir_name + folder_dir

    twitter = helpers.read_file(path + "twitter.txt")
    reddit = helpers.read_file(path + "reddit.txt")

    policies_prepro = preprocessing.full_preproccessing([twitter, reddit])
    policies = [twitter, reddit]

    corr_og = correlation.correlation_matrix(policies, ["twitter", "reddit"])
    corr_prepro = correlation.correlation_matrix(policies_prepro, ["twitter", "reddit"])

    print("######## Original files #########")
    correlation.print_correlation_matrix(corr_og)
    print("######## Preprocessed files #########")
    correlation.print_correlation_matrix(corr_prepro)


# Comparison Twitter reddit, correlation matrixp
compare_twitter_reddit_correlation(1, 1)
