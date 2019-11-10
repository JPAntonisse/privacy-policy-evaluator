from privacy_policy_evaluator import helpers, wordscoring
import matplotlib.pyplot as plt
import numpy as np

# Settings
files = [
    "../privacy_policy_evaluator/data/policies/google.txt",
    "../privacy_policy_evaluator/data/policies/reddit.txt",
    "../privacy_policy_evaluator/data/policies/twitter.txt",
    "../privacy_policy_evaluator/data/policies/ing.txt",
    "../privacy_policy_evaluator/data/policies/heineken.txt",
    "../privacy_policy_evaluator/data/policies/icloud.txt",
]

texts = []
for file in files:
    texts.append(helpers.read_file(file))

scores = []
for text in texts:
    scores.append(wordscoring.score_text(text).get('mean_privacy_norm'))

label = [r'$s={0:.3g}$'.format(score) for score in scores]

plt.figure(figsize=(7, 5), dpi=200)
plt.bar(range(len(scores)), scores, align='center', color='#F28444', width=0.8)

for i in range(len(scores)):
    plt.text(x=i - 0.4, y=scores[i] + 0.015, s=label[i], size=10)

plt.xticks(np.arange(len(scores)), (
    r'$google$',
    r'$reddit$',
    r'$twitter$',
    r'ing',
    r'heineken',
    r'icloud',
))
plt.yticks([x for x in np.arange(0, 1.1, 0.1)])
# plt.yticks(np.arange(0, 1.1, 0.1))
# plt.ylim(0, 1)
plt.ylabel(r'$\mu$ privacy score $s$', fontweight='bold')
plt.xlabel('Company', fontweight='bold')
plt.show()
