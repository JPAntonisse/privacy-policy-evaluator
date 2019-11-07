from os import listdir
from os.path import isfile, join


def split(text, delim=','):
    """
    Split a string into an array
    :param text:
    :param delim:
    :return:
    """
    return [x.strip() for x in text.split(delim)]


def read_file(file):
    """
    Reads a file and returns the text
    :param file:
    :return:
    """
    f = open(file, "r")
    return f.read()


def read_folder(folder):
    """
    Reads complete folder
    :param folder:
    :return:
    """
    file_names = [f for f in listdir(folder) if isfile(join(folder, f))]
    policies = []
    for file_name in file_names:
        f = open(folder + file_name, "r")
        policies.append(f.read())
    return policies
