import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd


def remove_enters(text):
    return text.replace('\n\n\n\n\n', '. ') \
        .replace('\n\n\n\n', '. ') \
        .replace('\n\n\n', '. ') \
        .replace('\n\n', '. ') \
        .replace('\n', '. ') \
        .replace('..', '.') \



def remove_abbreviations(text):
    text = " ".join(text.split())
    # remove ' such as I've, I'm etc.
    return text.replace("'ve", ' have')  \
                .replace("'m", ' am')    \
                .replace("'s", ' is')    \
                .replace("'t", ' not')   \
                .replace("'ll", ' will') \
                .replace("'re", ' are')  \



def replace_companies(text, company_names):
    text = " ".join(text.split())
    # Remove company names
    return text\
        .replace('Twitter', 'company')\
        .replace('Reddit', 'company')\
        .replace('twitter', 'company')\
        .replace('Apple', 'company')\
        .replace('Google', 'company')\
        .replace('ING', 'company')\
        .replace('Heineken', 'company')\
        .replace('reddit', 'company')


# remove special characters, basically removing all non letters and non spaces
def replace_str_index(text, index=0, replacement=' '):
    return '%s%s%s' % (text[:index], replacement, text[index + 1:])


def remove_special_chars(text):
    # find non letters and spaces and change them to a space.
    for i in range(0, len(text)):
        if not text[i].isalpha() and not text[i] == ' ' and not text[i] == '.':
            text = replace_str_index(text, i)
    return text


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


def lemmatization(text):
    sno = WordNetLemmatizer()
    lemmatized_policy_text = ''
    for word in text.split():
        lemmatized_policy_text += sno.lemmatize(word) + ' '
    return lemmatized_policy_text


def remove_stopwords(text):
    nltk_words = list(stopwords.words('english'))
    stop_words_removed_policy_text = ''
    for word in text.split():
        if not word in nltk_words:
            stop_words_removed_policy_text += word + ' '
    return stop_words_removed_policy_text


def full_preproccessing(documents, company_names=None, verbose=0):
    preprocessed = []
    count = 0
    for document in documents:
        if verbose > 0:  print(f'##########[Start preprocessing Document: {count}]##########')
        if verbose > 0:  print('----------[Removing Enters]----------')
        document = remove_enters(document)
        if verbose > 0:  print('----------[Removing Company names]----------')
        if company_names is not None:
            document = replace_companies(document, company_names)
        if verbose > 0:  print('----------[Removing special chars]----------')
        document = remove_special_chars(document)
        if verbose > 0:  print('----------[Removing modal verbs]----------')
        document = generalize_modal_verbs(document)
        if verbose > 0:  print('----------[Lemmatization]----------')
        document = lemmatization(document)
        if verbose > 0:  print('----------[Removing stop words]----------')
        document = remove_stopwords(document)

        count += 1
        preprocessed.append(document)

    return preprocessed
