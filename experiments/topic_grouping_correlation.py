from privacy_policy_evaluator import helpers, wordscoring, paragraphing, topic_grouper, correlation
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

topics = ['location', 'address', 'email', 'information']

texts = []  # Read File
for file in files:
    texts.append(helpers.read_file(file))

grouped = []
for text in texts:
    # Paragraph the given text
    paragraphed = paragraphing.paragraph(text)
    # Do the grouping
    grouped.append(topic_grouper.group(paragraphed, topics, 0.1))

a = [
    grouped[0].get('location'),
    grouped[0].get('address'),
    grouped[0].get('email'),
    grouped[0].get('information'),
    grouped[1].get('location'),
    grouped[1].get('address'),
    grouped[1].get('email'),
    grouped[1].get('information'),
]

corr_og = correlation.correlation_matrix(a)
correlation.print_correlation_matrix(corr_og)

f = plt.figure(figsize=(7, 5), dpi=200)
# plt.matshow(df.corr(), fignum=f.number)
# plt.xticks(range(df.shape[1]), df.columns, fontsize=14, rotation=45)
# plt.yticks(range(df.shape[1]), df.columns, fontsize=14)
# cb = plt.colorbar()
# cb.ax.tick_params(labelsize=14)
# plt.title('Correlation Matrix', fontsize=16);
