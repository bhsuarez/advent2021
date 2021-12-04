import csv


def load_advent_input_as_list(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def load_advent_input_as_dict(filename):
    index = 0
    file_dict = {}
    with open(filename, newline='') as f:
        for line in csv.reader(f):
            file_dict[index]=line[0]
            index += 1
    return file_dict