from privacy_policy_evaluator import commands

from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.pyplot as plt
from nltk.util import ngrams
import matplotlib as mpl
import numpy as np
import nltk

# settings
plt.figure(figsize=(15, 15))

def main(args=None):
    args = commands.parser.parse_args(args)
    try:
        func = args.func
    except AttributeError:
        pass
    else:
        func(args)


if __name__ == '__main__':
    main(['-h'])
