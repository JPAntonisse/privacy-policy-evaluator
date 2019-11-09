import numpy as np

from privacy_policy_evaluator import helpers, paragraphing, topic_grouper

# Settings
file = "../privacy_policy_evaluator/data/policies/reddit.txt"
topics = ['location']
# Thresholds
thresholds = [x for x in np.arange(0.025, 0.225, 0.025)]

# Read file
text = helpers.read_file(file)

# Print settings
print('Setting threshold range to: ' + str(thresholds))

res = []
for threshold in thresholds:
    # Paragraph the given text
    paragraphed = paragraphing.paragraph(text)
    # Get topics from argumnets
    grouped = topic_grouper.group(paragraphed, topics, threshold)
    # Score each topic on associated text
    scored_topics = topic_grouper.evaluate(grouped)

