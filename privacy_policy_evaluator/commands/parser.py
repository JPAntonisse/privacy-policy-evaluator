import argparse

parser = argparse.ArgumentParser(
    description='Privacy Policy Evaluator',
)
parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

subparsers = parser.add_subparsers(
    title='Commands',
    dest='function',
    help='Help',
)
parser_difference = subparsers.add_parser('compare',
                                          help='ppe.py compare {txt1} {txt2}: Show the difference of two texts')
parser_difference.add_argument('txt1', type=str, help='Base text')
parser_difference.add_argument('txt2', type=str, help='Compare text')

parser_difference = subparsers.add_parser('evaluate',
                                          help='ppe.py evaluate {text} [--topic] Evaluate document')
parser_difference.add_argument('text', type=str, help='Text to evaluate')
parser_difference.add_argument('--topic', type=str, help='json file for topics')
