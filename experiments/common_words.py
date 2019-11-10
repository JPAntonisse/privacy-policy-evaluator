from privacy_policy_evaluator import helpers, wordscoring, paragraphing, topic_grouper, preprocessing
import matplotlib.pyplot as plt
import numpy as np

# Settings
files = [
    "../privacy_policy_evaluator/data/policies/google.txt",
    "../privacy_policy_evaluator/data/policies/reddit.txt",
    "../privacy_policy_evaluator/data/policies/twitter.txt",
    "../privacy_policy_evaluator/data/policies/ing.txt",
    "../privacy_policy_evaluator/data/policies/icloud.txt",
]


text = ''
for file in files:
    file =  helpers.read_file(file)
    text = text + preprocessing.full_preproccessing([file], 1)[0]

text = helpers.remove_stop_words(text)

print(helpers.most_common_words(text, 50))


