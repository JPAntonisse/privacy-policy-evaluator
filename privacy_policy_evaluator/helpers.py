from os import listdir
from os.path import isfile, join


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
