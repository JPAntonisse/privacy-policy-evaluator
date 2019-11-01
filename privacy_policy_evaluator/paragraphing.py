import numpy as np


def paragraphing(text):
    # Split file on lines
    text_lines = [s.strip() for s in text.splitlines()]
    # Sort the line length
    text_length = sorted([len(s) for s in text_lines if len(s) < 250])
    # Get the Gradient
    text_gradient = np.gradient(text_length, 2)
    # Get first position where grad > 2
    text_pos = next(x[0] for x in enumerate(text_gradient) if x[1] > 4)
    # Split and set rejection and text
    text_split = text_length[text_pos]
    #  Set Accepted and Rejected
    text_accepted = [s for s in text_lines if len(s) >= text_split]
    text_rejected = [s for s in text_lines if len(s) < text_split]
    # Return
    return [text_accepted, text_rejected]

    # # Print Policy Paragraph
    # for idx, item in enumerate(text_accepted):
    #     f = open("data/policies/paragraphed/reddit-" + str(idx) + ".txt", "w")
    #     f.write(item)
    #     f.close()

    # # Plot the sorted length of each line
    # plt.figure(figsize=(15, 15))
    # plt.xlabel('Lines sorted on size from small to large')
    # plt.ylabel('Length of line len(string)')
    # plt.grid()
    # plt.plot(twitter_grad, label='twitter gradient')
    # plt.plot(reddit_grad, label='reddit gradient')
    #
    # plt.plot(twitter_length, label='Twitter paragraph length')
    # plt.plot(reddit_length, label='Reddit paragraph length')
    # plt.axhline(y=2, color='black', linestyle=':', label=r'$y=2$')
    #
    # plt.axvline(x=twitter_pos, color='g', linestyle=':',
    #             label=r'Twitter acceptance point $y=' + str(twitter_split) + '$')
    # plt.axvline(x=reddit_pos, color='r', linestyle=':', label=r'Reddit acceptance point $y=' + str(reddit_split) + '$')
    # plt.legend()


twitter = open("data/policies/twitter.txt","r").read()
paragraphing(twitter)