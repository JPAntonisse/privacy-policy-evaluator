import argparse

parser = argparse.ArgumentParser('python-boilerplate')
parser.add_argument('--version', '-v', action='version',
                    version='%(prog)s 1.0.0')
subparsers = parser.add_subparsers(
    title='subcommands',
    description='valid subcommands',
    help='sub-command help',
)