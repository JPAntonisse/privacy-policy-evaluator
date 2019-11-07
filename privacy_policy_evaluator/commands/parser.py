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
                                          help='ppe.py compare {file1} {file2}: Show the difference of two texts')
parser_difference.add_argument('file1', type=str, help='Base file')
parser_difference.add_argument('file2', type=str, help='Compare file')


parser_difference = subparsers.add_parser(
    'evaluate',
    help='ppe.py evaluate {file} [--topic] Evaluate document'
)
parser_difference.add_argument(
    'file',
    type=str,
    help='Text file to evaluate'
)
parser_difference.add_argument(
    '--topic',
    type=str,
    help='--topic example1,example2: Evaluate document on specified topic(s)'
)
