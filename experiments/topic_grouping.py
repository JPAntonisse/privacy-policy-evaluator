from privacy_policy_evaluator import helpers, wordscoring, paragraphing, topic_grouper
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

texts = [] # Read File
for file in files:
    texts.append(helpers.read_file(file))


scores = []
for text in texts:
    # Paragraph the given text
    paragraphed = paragraphing.paragraph(text)
    # Do the grouping
    grouped = topic_grouper.group(paragraphed, topics, 0.1)
    # Score each topic on associated text
    scores.append(topic_grouper.evaluate(grouped))


# set width of bar
barWidth = 0.2

# Set position of bar on X axis
r1 = np.arange(len(scores))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

plt.figure(figsize=(7, 5), dpi=200)

# Make the plot
plt.bar(r1, [score.get('information').get('mean_privacy_norm') for score in scores], color='#F2AC57', width=barWidth, edgecolor='white', label='Information')
plt.bar(r2, [score.get('location').get('mean_privacy_norm') for score in scores], color='#F28444', width=barWidth, edgecolor='white', label='Location')
plt.bar(r3, [score.get('address').get('mean_privacy_norm') for score in scores], color='#F24141', width=barWidth, edgecolor='white', label='Address')
plt.bar(r4, [score.get('email').get('mean_privacy_norm') for score in scores], color='#0D0D0D', width=barWidth, edgecolor='white', label='Email')
# plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='var2')
# plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')


# Add xticks on the middle of the group bars
plt.xlabel('Company', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(scores))], ['Google', 'Reddit', 'Twitter', 'ING', 'iCloud'])
plt.yticks([x for x in np.arange(0, 1.1, 0.1)])
plt.ylabel(r'$\mu$ privacy score', fontweight='bold')
# Create legend & Show graphic
plt.legend()
plt.show()


#
# label = [r'$s={0:.3g}$'.format(score) for score in scores]
#
# plt.figure(figsize=(7, 7), dpi=200)
# plt.bar(range(len(scores)), scores, align='center', width=0.8)
#
# for i in range(len(scores)):
#     plt.text(x=i - 0.4, y=scores[i] + 0.0005, s=label[i], size=10)
#
# plt.xticks(np.arange(len(scores)), (
#     r'$google$',
#     r'$reddit$',
#     r'$twitter$',
#     r'ing',
#     r'heineken',
#     r'icloud',
# ))
#
# # plt.yticks(np.arange(0, 1.1, 0.1))
# # plt.ylim(0, 1)
# plt.ylabel(r'Score $s$')
# plt.xlabel('Company')
# plt.show()
