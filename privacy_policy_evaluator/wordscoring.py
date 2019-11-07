# Multiplier to determine the statement.
import json

# If setting names are changed within 'settings.json' file, they also need to be changed here.
normTotalWords = "normalizedTotalWords"
normSpecialWords = "normalizedSpecialWords"
min_score = "min"
max_score = "max"


def score_text(text):
    statements = text.split('.')

    # remove empty statements
    statements = [x for x in statements if len(x) > 0]
    # Strip spaces
    statements = [x.strip() for x in statements]

    dictPrivacyWords = jsonReaderPrivacyWordScores()
    dictSettings = jsonReaderSettings()

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

        print(statement_rating)
        total_statement_rating += statement_rating

    print("Total statement rating: ", total_statement_rating)
    avg_privacy_word_score = total_statement_rating / total_privacy_word_count
    print("Avg. score per privacy word ", avg_privacy_word_score)

    # Check if we have to normalize the score
    if dictSettings[normSpecialWords]:
        # In this case the values are between 0 and 10 through which dividing it by 10 will
        avg_privacy_word_score = avg_privacy_word_score / 10
        print("(Norm.) Avg. score per privacy word ", avg_privacy_word_score)

    # asdf = total_statement_rating / len(statements)
    # print(asdf)


def jsonReaderSettings():
    dict = {}

    with open('data/settings.json') as json_file:
        data = json.load(json_file)
        settings = data['settings']
        for element in settings:
            if element != 'data':
                dict[element] = settings[element]

    return dict


def jsonReaderPrivacyWordScores():
    dict = {}

    with open('data/settings.json') as json_file:
        data = json.load(json_file)
        for p in data['settings']['data']:
            for i in range(0, len(data['settings']['data'][p]['words'])):
                dict[data['settings']['data'][p]['words'][i]] = data['settings']['data'][p]['value']
    return dict
