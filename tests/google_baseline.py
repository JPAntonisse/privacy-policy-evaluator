from privacy_policy_evaluator import helpers, wordscoring
import matplotlib.pyplot as plt
import numpy as np

# Settings
file = "../privacy_policy_evaluator/data/policies/google.txt"

# Read file
text = helpers.read_file(file)

# Get the Score
score = wordscoring.score_text(text)
score = [
    score.get('mean'),
    score.get('mean_norm'),
]

label = [r'$s={0:.3g}$'.format(num) for num in score]

print(score)
plt.figure(figsize=(7, 7), dpi=200)
plt.bar(range(len(score)), score, align='center', width=0.8)

for i in range(len(score)):
    plt.text(x=i-0.15, y=score[i] + 0.02, s=label[i], size=10)

plt.xticks(np.arange(len(score)), (
    r'$\mu$',
    r'$\mu$ normalized',
))

plt.yticks(np.arange(0, 1.1, 0.1))
plt.ylim(0, 1)
plt.ylabel(r'Score $s$')
plt.xlabel('Mean score')
plt.title('Google Privacy Policy Word Scoring')
plt.show()
