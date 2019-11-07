# Multiplier to determine the statement.
import json

def score_text(text):
    statements = text.split('.')

    # remove empty statements
    statements = [x for x in statements if len(x) > 0]

    # Stip spaces
    statements = [x.strip() for x in statements]
    # - * - = - in dit geval
    dictPrivacyWords = jsonReader()
    # Print the statements
    total_statement_rating = 0
    norm_total_statement_rating = 0
    for statement in statements:
        # print(statement)
        statement_rating = 1
        norm_statement_rating = 0
        for word in statement.split():
            if word in dictPrivacyWords:
                statement_rating += dictPrivacyWords[word]
        # print(statement_rating)
        total_statement_rating += statement_rating / (len(statement.split()) if len(statement.split()) > 0 else 1)
    asdf = total_statement_rating / len(statements)
    print(asdf)

def jsonReader():
    dict = {}

    with open('data/settings.json') as json_file:
        data = json.load(json_file)
        for p in data['settings']['data']:
            #print(data['settings']['data'][p]['words'][0])
            for i in range(0, len(data['settings']['data'][p]['words'])):
                dict[data['settings']['data'][p]['words'][i]] = data['settings']['data'][p]['value']
    return dict

jsonReader()