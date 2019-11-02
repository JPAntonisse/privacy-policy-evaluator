twitter_policy = open("policies/pre-processed/twitter_2.txt","r")
policy_text = twitter_policy.read()

#Multiplier to determine the statement.

statements = policy_text.split('.')

# remove empty statements
statements = [x for x in statements if len(x) > 0]

# Stip spaces
statements = [x.strip() for x in statements]

word_multiplier_dict = {
    "access" : -5,
    "aggregate" : -2,
    "allow" : -3,
    "apply" : -2,
    "avoid" : 3,
    "block" : 5,
    "change" : -2,
    "choose" : 3,
    "collect" : -5,
    "comply" : -3,
    "connect" : -2,
    "consolidate" : -2,
    "contact" : -4,
    "contract" : -4,
    "customize" : -5,
    "deny" : -5,
    "destroy" : -10,
    "disallow" : 3,
    "discipline" : -2,
    "disclaim" : -4,
    "disclose" : -4,
    "display" : -4,
    "enforce" : -10,
    "ensure" : 2,
    "exchange" : -7,
    "help" : 5,
    "honor" : -2,
    "imply" : -2,
    "inform" : 5,
    "limit" : -5,
    "maintain" : 3,
    "make" : -2,
    "maximize" : -5,
    "minimize" : 5,
    "monitor" : -10,
    "notify" : 3,
    "obligate" : -10,
    "opt-in" : 4,
    "opt-out" : -4,
    "investigate" : -5,
    "post" : -5,
    "prevent" : 3,
    "prohibit" : -5,
    "protect" : 5,
    "provide" : -5,
    "recommend" : 2,
    "request" : 5,
    "require" : -5,
    "reserve" : -2,
    "review" : 2,
    "share" : -10,
    "specify" : 2,
    "store" : -8,
    "update" : -6,
    "urge" : 2,
    "use" : -5,
    "verify" : 3,
    "prohibition" : -5,
    "permission" : 5,
    "obligation" : -5,
    "anti-obligation" : 5
}

#- * - = - in dit geval

# Print the statements
total_statement_rating = 0
norm_total_statement_rating = 0
for statement in statements:
    #print(statement)
    statement_rating = 1
    norm_statement_rating = 0
    for word in statement.split():
        if word in word_multiplier_dict:
            norm_statement_rating+=1
            if statement_rating < 0 and word_multiplier_dict[word] < 0: statement_rating = statement_rating + word_multiplier_dict[word]
            elif word_multiplier_dict[word] > 0: statement_rating = statement_rating + word_multiplier_dict[word]
            else: statement_rating += word_multiplier_dict[word]
    total_statement_rating += statement_rating / ( norm_statement_rating if norm_statement_rating > 0 else 1 )
text_grade_score = total_statement_rating / len(statements)
print(text_grade_score)