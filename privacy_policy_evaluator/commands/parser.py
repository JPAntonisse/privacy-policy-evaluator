import argparse

parser = argparse.ArgumentParser(
    description='Privacy Policy Evaluator',
)
parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')

subparsers = parser.add_subparsers(
    title='Privacy Policy Evaluator',
    description='Commands',
    dest='function',
    help='Description',
)
#
# create the parser for the "a" command
parser_difference = subparsers.add_parser('difference', help='Show the difference of two documents')
parser_difference.add_argument('doc1', type=str, help='Base Document')
parser_difference.add_argument('doc2', type=str, help='Document to compare with')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')
