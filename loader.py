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
            index += 1
            if index > 1:
                file_dict[index]=line[0]
    return file_dict