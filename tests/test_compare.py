import os

text1 = "../privacy_policy_evaluator/data/policies/reddit.txt"
text2 = "../privacy_policy_evaluator/data/policies/twitter.txt"


def compare():
    os.system("python ../ppe.py compare " + text1 + " " + text2)


def evaluate():
    os.system("python ../ppe.py evaluate " + text1)


def evaluate_on_topic():
    os.system("python ../ppe.py evaluate " + text1 + " --topic location,data,your")


evaluate_on_topic()
# evaluate()
# compare()
# evaluate_on_topic()
# print(os.path.dirname(os.path.abspath(__file__)))
