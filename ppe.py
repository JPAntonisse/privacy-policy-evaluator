from privacy_policy_evaluator import paragraphing, commands, preprocessing, helpers, correlation, wordscoring, topic_grouper
from typing import Callable


def main(args=None):
    """
    Main Starting Code
    """
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
    Evaluate a given file, if a topic is set, do a score on topic
    """
    if args.topic:
        evaluate_on_topic(args)
    else:
        evaluate_score(args)


def evaluate_on_topic(args):
    """
    Evaluate a given document on certain topics.
    Paragraphs that describe a certain topics are associated with that topic
    After which all associated topics are scored based on the extracted text
    :param args:
    """
    # Read textfile
    text = helpers.read_file(args.file)
    # Paragraph the given text
    paragraphed = paragraphing.paragraph(text)
    # Get topics from argumnets
    topics = helpers.split(args.topic)
    # Do the grouping
    grouped = topic_grouper.group(paragraphed, topics, 0.1)
    # Score each topic on associated text
    scored_topics = topic_grouper.evaluate(grouped)

    # for key, value in d.items():
    print(scored_topics)


def evaluate_score(args):
    """
    Evaluate a score
    :param args:
    """
    # Read textfile
    text = helpers.read_file(args.file)
    # Get the Score
    score = wordscoring.score_text(text)
    print(score)


def compare(args):
    """
    Compare two given text
    """
    # Read the files
    text1 = helpers.read_file(args.file1)
    text2 = helpers.read_file(args.file2)

    # Prepreocessing
    policies = preprocessing.full_preproccessing([text1, text2])

    # Do the compare
    df = correlation.correlation_matrix(policies)
    # Print the compare
    correlation.print_correlation_matrix(df)


if __name__ == '__main__':
    main()
