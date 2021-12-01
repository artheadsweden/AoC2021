def read_input_as_int(filename):
    with open(filename, 'r', encoding='utf-8') as infile:
        return [int(line.strip()) for line in infile.readlines()]


def read_input_as_str(filename):
    with open(filename, 'r', encoding='utf-8') as infile:
        return [line.strip() for line in infile.readlines()]