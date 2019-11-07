from privacy_policy_evaluator import commands
from typing import Callable


def main(args=None):
    # Parse input
    args = commands.parser.parse_args(args)
    # Select the function in this document that is the first argument
    arg_func: Callable = globals()[args.function]
    # Call the funciton
    arg_func(args)


def evaluate(args):
    """
    Evaluate a given text
    """
    print('eval')


def compare(args):
    # DO the difference
    print(args)


if __name__ == '__main__':
    main()
