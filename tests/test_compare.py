import os

text1 = "../privacy_policy_evaluator/data/policies/reddit.txt"
text2 = "../privacy_policy_evaluator/data/policies/twitter.txt"

out = "output_weighted.png"
filter_type = 0
os.system("python ../ppe.py compare " + text1 + " " + text2)