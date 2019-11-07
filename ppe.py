from privacy_policy_evaluator import commands
from typing import Callable


def main(args=None):
    # Parse input
    args = commands.parser.parse_args(args)
    # Select the function in this document that is the first argument
    arg_func: Callable = globals()[args.function]
    # Call the funciton
    arg_func()


def difference():
    # DO the difference
    print('aa')


if __name__ == '__main__':
    main()
