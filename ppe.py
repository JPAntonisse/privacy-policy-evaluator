from privacy_policy_evaluator import commands, preprocessing, helpers, correlation
from typing import Callable


def main(args=None):
    # Parse input
    args = commands.parser.parse_args(args)
    try:
        # Select the function in this document that is the first argument
        arg_func: Callable = globals()[args.function]
        # Call the funciton
        arg_func(args)
    except KeyError:
        commands.parser.parse_args(['-h'])
        pass


def evaluate(args):
    """
    Evaluate a given text
    """
    # Give company name
    # full_preprocessing

    print('eval')


def compare(args):
    """
    Compare two given text
    """
    # Read the files
    text1 = helpers.read_file(args.text1)
    text2 = helpers.read_file(args.text2)

    # Prepreocessing
    policies = preprocessing.full_preproccessing([text1, text2])

    # Do the compare
    df = correlation.correlation_matrix(policies)
    # Print the compare
    correlation.print_correlation_matrix(df)


if __name__ == '__main__':
    main()
