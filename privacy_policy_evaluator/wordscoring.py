# Multiplier to determine the statement.
import json, os
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# If setting names are changed within 'settings.json' file, they also need to be changed here.
# min, max for normalization. What is the highest valued words and the lowest valued word
min_score = "min"
max_score = "max"


def score_text(text, verbose = 0):
    statements = text.split('.')

    # remove empty statements
    statements = [x for x in statements if len(x) > 0]
    # Strip spaces
    statements = [x.strip() for x in statements]

    dictPrivacyWords = json_read_privacy_word_scores()
    dictSettings = json_read_settings()

    # Print the statements
    total_statement_rating = 0
    norm_total_statement_rating = 0

    # Keep track of total number of privacy words that occur in text
    total_privacy_word_count = 0
    for statement in statements:
        statement_rating = 0

        # Keep track of number of privacy words per sentence
        # Currently this variable has no function at all
        statement_privacy_word_count = 0

        for word in statement.split():
            if word in dictPrivacyWords:
                statement_privacy_word_count += 1
                total_privacy_word_count += 1
                statement_rating += dictPrivacyWords[word]

        # print(statement_rating)
        total_statement_rating += statement_rating

    avg_privacy_word_score = total_statement_rating / total_privacy_word_count
    norm_avg_privacy_word_score = avg_privacy_word_score / (dictSettings[max_score] - dictSettings[min_score])
    avg_score_total_words = total_statement_rating / len(text.split())
    norm_avg_score_total_words = avg_score_total_words / (dictSettings[max_score] - dictSettings[min_score])

    if verbose > 0:
        print("Total statement rating: ", total_statement_rating)
        print("Avg. score per privacy word ", avg_privacy_word_score)
        print("(Norm.) Avg. score per privacy word ", norm_avg_privacy_word_score)
        print("Avg. score per total word", avg_score_total_words)
        print("(Norm.) Avg. score per privacy word total ", norm_avg_score_total_words)

    return {
        "total": total_statement_rating,
        "mean": avg_score_total_words,
        "mean_norm": norm_avg_score_total_words,
        "mean_privacy": avg_privacy_word_score,
        "mean_privacy_norm": norm_avg_privacy_word_score,
    }


def json_read_settings():
    dict = {}

    with open(os.path.dirname(os.path.abspath(__file__)) + '/data/settings.json') as json_file:
        data = json.load(json_file)
        settings = data['settings']
        for element in settings:
            if element != 'data':
                dict[element] = settings[element]

    return dict


def json_read_privacy_word_scores():
    dict = {}

    with open(os.path.dirname(os.path.abspath(__file__)) + '/data/settings.json') as json_file:
        data = json.load(json_file)
        for p in data['settings']['data']:
            for i in range(0, len(data['settings']['data'][p]['words'])):
                dict[data['settings']['data'][p]['words'][i]] = data['settings']['data'][p]['value']
    return dict


def plot_result():
    reddit = open(os.path.dirname(os.path.abspath(__file__)) + '/data/policies/reddit.txt',"r", encoding="utf8").read()
    reddit_dict = score_text(reddit)

    twitter = open(os.path.dirname(os.path.abspath(__file__)) + '/data/policies/twitter.txt',"r", encoding="utf8").read()
    twitter_dict = score_text(twitter)

    bankofamerica = open(os.path.dirname(os.path.abspath(__file__)) + '/data/policies/bankofamerica.txt',"r", encoding="utf8").read()
    bankofamerica_dict = score_text(bankofamerica)

    ing = open(os.path.dirname(os.path.abspath(__file__)) + '/data/policies/ing.txt',"r", encoding="utf8").read()
    ing_dict = score_text(ing)

    deutschebank = open(os.path.dirname(os.path.abspath(__file__)) + '/data/policies/deutschebank.txt',"r", encoding="utf8").read()
    deutschebank_dict = score_text(deutschebank)

    heineken = open(os.path.dirname(os.path.abspath(__file__)) + '/data/policies/heineken.txt',"r", encoding="utf8").read()
    heineken_dict = score_text(heineken)

    total_score = [reddit_dict["total"], twitter_dict["total"], bankofamerica_dict["total"],
         ing_dict["total"], deutschebank_dict["total"], heineken_dict["total"]]

    mean = [reddit_dict["mean"], twitter_dict["mean"], bankofamerica_dict["mean"], ing_dict["mean"],
         deutschebank_dict["mean"], heineken_dict["mean"]]

    mean_norm = [reddit_dict["mean_norm"], twitter_dict["mean_norm"], bankofamerica_dict["mean_norm"],
         ing_dict["mean_norm"], deutschebank_dict["mean_norm"], heineken_dict["mean_norm"]]

    mean_privacy = [reddit_dict["mean_privacy"], twitter_dict["mean_privacy"], bankofamerica_dict["mean_privacy"],
         ing_dict["mean_privacy"], deutschebank_dict["mean_privacy"], heineken_dict["mean_privacy"]]

    mean_privacy_norm = [reddit_dict["mean_privacy_norm"], twitter_dict["mean_privacy_norm"], bankofamerica_dict["mean_privacy_norm"],
                    ing_dict["mean_privacy_norm"], deutschebank_dict["mean_privacy_norm"], heineken_dict["mean_privacy_norm"]]

    objects = ('Reddit', 'Twitter', 'Bank of America', 'ING', 'Deutsche Bank', 'Heineken')
    y_pos = np.arange(len(objects))

    #plt.bar(y_pos, total_score, align='center', alpha=0.4)

    plt.figure(figsize=(8, 5))  # width:20, height:3
    plt.bar(range(len(objects)), mean_privacy, align='center', width=0.8, color='black')

    plt.xticks(y_pos, objects)
    plt.ylabel('Average score per privacy word')
    plt.xlabel('Policy')
    plt.title('Average score per privacy word vs different policies')


    plt.show()

#plot_result()