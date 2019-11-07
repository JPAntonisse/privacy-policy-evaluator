# imports
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd

# Plot Settings
import matplotlib.pyplot as plt
import matplotlib

plt.rcParams["figure.figsize"] = (20, 10)
font = {'family': 'normal',
        'weight': 'bold',
        'size': 22}

matplotlib.rc('font', **font)

# Location policies of companies
twitter_policy = "We require information  about  your  signup  and  current  location,  which  we get from signals such as your IP address or device settings, to securely and reliably set up and maintain your account and to provide our services to you.Subject to your settings, we may collect, use, and store additional infor-mation about your location - such as your current precise position or placeswhere you’ve previously used Twitter - to operate or personalize our servicesincluding with more relevant content like local trends, stories, ads, and sug-gestions  for  people  to  follow.   Learn  more  about  Twitter’s  use  of  locationhere,  and  how  to  set  your  Twitter  location  preferences  here.   Learn  moreabout how to share your location in Periscope broadcasts here."
reddit_policy = "We may receive and process information about your location. For example, with your consent, we may collect information about the specific location of your mobile device (for example, by using GPS or Bluetooth). We may also receive location information from you when you choose to share such information on our Services, including by associating your content with a location, or we may derive your approximate location from other information about you, including your IP address."
tumblr_policy = "In some cases we collect and store information about where you are located, such as by converting your IP Address into a rough geolocation. We may also ask you to provide information about your location, for example permission to use your geolocation information from your mobile device to geotag a post. We may use location information to improve and personalize the Services for you, for example by showing you relevant local content."
nine_gag_policy = "When you use our services, we may collect information about your location. With your permission, we may also collect information about your precise location using methods that include GPS, wireless networks, and Wi-Fi access points."

# Select a policy text
twitter_policy = open("policies/reddit.txt", "r")
policy_text = twitter_policy.read()


# print(twitter_policy.read())
# policy_text = twitter_policy
def remove_enters(text):
    return text.replace('\n\n\n\n\n', '. ').replace('\n\n\n\n', '. ').replace('\n\n\n', '. ').replace('\n\n',
                                                                                                      '. ').replace(
        '\n', '. ').replace('..', '.')


policy_text = remove_enters(policy_text)

print('----------[Original text]----------')
print(policy_text)


# %%latex
# Replace 've with have, 'm with am etc.
# Replace Company Names with $company$

# In[159]:


def replace_companies(text):
    text = " ".join(text.split())
    # remove ' such as I've, I'm etc.
    text = text.replace("'ve", ' have').replace("'m", ' am').replace("'s", ' is').replace("'t", ' not').replace("'ll",
                                                                                                                ' will').replace(
        "'re", ' are')
    # Remove company names
    return text.replace('Twitter', 'company').replace('Reddit', 'company').replace('twitter', 'company').replace(
        'reddit', 'company')


policy_text = replace_companies(policy_text)

print('----------[Company names replaced]----------')
print(policy_text)


# %%latex
# Remove special characters, only leave alphabetical and spacing.

# In[160]:


# remove special characters, basically removing all non letters and non spaces
def replace_str_index(text, index=0, replacement=' '):
    return '%s%s%s' % (text[:index], replacement, text[index + 1:])


def remove_special_chars(text):
    # find non letters and spaces and change them to a space.
    for i in range(0, len(text)):
        if not text[i].isalpha() and not text[i] == ' ' and not text[i] == '.':
            text = replace_str_index(text, i)
    return text


policy_text = remove_special_chars(policy_text)

print('----------[Remove everything except spaces and letters]----------')
print(policy_text)


def generalize_modal_verbs(text):
    # Replace text with Anti-obligation
    text = text.replace('is not required to', 'anti-obligation')
    # Replace text with Prohibition
    text = text.replace('does not have a right to', 'prohibition').replace('does not', 'prohibition').replace('do not',
                                                                                                              'prohibition').replace(
        'will not', 'prohibition')
    # Replace text with Obligation
    text = text.replace('may not require', 'obligation').replace('may not', 'obligation').replace('must deny',
                                                                                                  'obligation').replace(
        'must permit', 'obligation').replace('must request', 'obligation').replace('must', 'obligation')
    # Replace text with Permissions
    text = text.replace('has a right to', 'permission').replace('may deny', 'permission').replace('may require',
                                                                                                  'permission').replace(
        'may', 'permission').replace('retains the right to', 'permission').replace('could', 'permission').replace('can',
                                                                                                                  'permission')
    return text.replace('e.g.', 'for example')


policy_text = generalize_modal_verbs(policy_text)


def lemmatization(text):
    sno = WordNetLemmatizer()
    lemmatized_policy_text = ''
    for word in text.split():
        lemmatized_policy_text += sno.lemmatize(word) + ' '
    return lemmatized_policy_text


policy_text = lemmatization(policy_text)

print('----------[Lemmatization]----------')
print(policy_text)


def remove_stopwords(text):
    nltk_words = list(stopwords.words('english'))
    stop_words_removed_policy_text = ''
    for word in text.split():
        if not word in nltk_words:
            stop_words_removed_policy_text += word + ' '
    return stop_words_removed_policy_text


policy_text = remove_stopwords(policy_text)

print('----------[Removing stop words]----------')
print(policy_text)

# In[ ]:


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

# In[152]:


# Set test text from Facebooks Policty
# policy_test = "Facebook and Instagram share infrastructure, systems and technology with other Facebook Companies (which include WhatsApp and Oculus) to provide an innovative, relevant, consistent and safe experience across all Facebook Company Products you use. We also process information about you across the Facebook Companies for these purposes, as permitted by applicable law and in accordance with their terms and policies. For example, we process information from WhatsApp about accounts sending spam on its service so we can take appropriate action against those accounts on Facebook, Instagram or Messenger. We also work to understand how people use and interact with Facebook Company Products, such as understanding the number of unique users on different Facebook Company Products."
policy_test = policy_text

# Split on Sentences
lines = policy_test.split('. ')

# Tokenize each line
tokens = [nltk.word_tokenize(str) for str in lines]

pos = [nltk.pos_tag(el) for el in tokens]

# print(pos)

fdist = nltk.FreqDist(tokens[0])
fdist.plot()

nltk.pos_tag(tokens)


# Read file

# Import statements

# Preprocess data

# Compare results



# Process Paragraphed files
files_path = "policies/paragraphed/"

policies_file_names = [f for f in listdir(files_path) if isfile(join(files_path, f))]
policy_company_names = [name.split('.')[0] for name in policies_file_names]

# Select a policy text
policies = []
for file_name in policies_file_names:
    f = open(files_path + file_name, "r")
    policies.append(f.read())

preprocessed = []
for (idx, policy) in enumerate(policies):
    policy = remove_enters(policy)
    policy = replace_companies(policy)
    policy = remove_special_chars(policy)
    policy = generalize_modal_verbs(policy)
    policy = lemmatization(policy)
    policy = remove_stopwords(policy)
    preprocessed.append(policy)

# Print Policy Paragraph
for idx, item in enumerate(preprocessed):
    f = open("policies/pre-processed/paragraphed/" + str(policy_company_names[idx]) + ".txt", "w+")
    f.write(item)
    f.close()
