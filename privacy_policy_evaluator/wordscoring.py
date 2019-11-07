# Multiplier to determine the statement.

statements = policy_text.split('.')

# remove empty statements
statements = [x for x in statements if len(x) > 0]

# Stip spaces
statements = [x.strip() for x in statements]

word_multiplier_dict = {
    "access": -2,
    "aggregate": -2,
    "allow": -2,
    "apply": -2,
    "avoid": -2,
    "block": -2,
    "change": -2,
    "choose": -2,
    "collect": -2,
    "comply": -2,
    "connect": -2,
    "consolidate": -2,
    "contact": -2,
    "contract": -2,
    "customize": -2,
    "deny": -2,
    "destroy": -2,
    "disallow": -2,
    "discipline": -2,
    "disclaim": -2,
    "disclose": -2,
    "display": -2,
    "enforce": -2,
    "ensure": -2,
    "exchange": -2,
    "help": -2,
    "honor": -2,
    "imply": -2,
    "inform": -2,
    "limit": -2,
    "maintain": -2,
    "make": -2,
    "maximize": -2,
    "minimize": -2,
    "monitor": -2,
    "notify": -2,
    "obligate": -2,
    "opt-in": -2,
    "opt-out": -2,
    "investigate": -2,
    "post": -2,
    "prevent": -2,
    "prohibit": -2,
    "protect": -2,
    "provide": -2,
    "recommend": -2,
    "request": -2,
    "require": -2,
    "reserve": -2,
    "review": -2,
    "share": -2,
    "specify": -2,
    "store": -2,
    "update": -2,
    "urge": -2,
    "use": -2,
    "verfy": -2,
    "prohibition": -2,
    "permission": 2,
    "obligation": -2,
    "anti-obligation": 2
}

# - * - = - in dit geval

# Print the statements
total_statement_rating = 0
norm_total_statement_rating = 0
for statement in statements:
    # print(statement)
    statement_rating = 1
    norm_statement_rating = 0
    for word in statement.split():
        if word in word_multiplier_dict:
            if statement_rating < 0 and word_multiplier_dict[word] < 0:
                statement_rating = statement_rating * abs(word_multiplier_dict[word])
            elif word_multiplier_dict[word] > 0:
                statement_rating = abs(statement_rating) * word_multiplier_dict[word]
            else:
                statement_rating *= word_multiplier_dict[word]
    # print(statement_rating)
    total_statement_rating += statement_rating / (len(statement.split()) if len(statement.split()) > 0 else 1)
asdf = total_statement_rating / len(statements)
print(asdf)