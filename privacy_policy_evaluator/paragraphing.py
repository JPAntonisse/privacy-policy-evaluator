import numpy as np


def paragraph(text):
    # Split file on lines
    text_lines = [s.strip() for s in text.splitlines()]
    # Sort the line length
    text_length = sorted([len(s) for s in text_lines if len(s) < 250])
    # Get the Gradient of linelength
    text_gradient = np.gradient(text_length, 2)
    # Get first position where grad > 4
    text_pos = next(x[0] for x in enumerate(text_gradient) if x[1] > 4)
    # Split and set rejection and text
    text_split = text_length[text_pos]
    #  Set Accepted and Rejected
    text_accepted = [s for s in text_lines if len(s) >= text_split]
    text_rejected = [s for s in text_lines if len(s) < text_split]
    return text_accepted
