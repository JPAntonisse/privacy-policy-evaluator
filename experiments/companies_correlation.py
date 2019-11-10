from privacy_policy_evaluator import helpers, wordscoring, paragraphing, topic_grouper, correlation
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# Settings
files = [
    "../privacy_policy_evaluator/data/policies/google.txt",
    "../privacy_policy_evaluator/data/policies/reddit.txt",
    "../privacy_policy_evaluator/data/policies/twitter.txt",
    "../privacy_policy_evaluator/data/policies/ing.txt",
    "../privacy_policy_evaluator/data/policies/icloud.txt",
]

companies = ['Google', 'Reddit', 'Twitter', 'ING', 'iCloud']

texts = []  # Read File
for file in files:
    texts.append(helpers.read_file(file))

df = correlation.correlation_matrix(texts)
df = df.loc[0:4, np.arange(0, 5)]
print(df)
correlation.print_correlation_matrix(df)

fig = plt.figure(figsize=(7, 5), dpi=200)
ax = fig.add_subplot(111)

nThresholds = 10
col = [(1, 1, 1), (242 / 255, 40 / 255, 38 / 255)]
cmap = colors.LinearSegmentedColormap.from_list(name='custom', colors=col)
cax = ax.matshow(df, interpolation='nearest', vmin=0, vmax=1, cmap=cmap)

cbar = fig.colorbar(cax)
cbar.ax.set_ylabel('Score', rotation=270)
ax.set_xticklabels([''] + companies)
ax.set_yticklabels([''] + companies)
ax.xaxis.tick_top()
ax.set_title('Company')
plt.ylabel('Company')
plt.show()
