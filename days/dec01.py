from utils import read_input_as_int


def sum_it(values: list):
    increase = 0
    old_value = None
    for value in values:
        if not old_value:
            old_value = value
        else:
            if old_value < value:
                increase += 1
            old_value = value
    return increase


def puzzle1(values: list):
    return sum_it(values)


def puzzle2(values: list):
    sums = []
    for value in range(len(values)):
        a_sum = 0
        for i in range(3):
            try:
                a_sum += values[value+i]
            except IndexError:
                break
        sums.append(a_sum)
    return sum_it(sums)


def main():
    values = read_input_as_int('data/input_dec01.txt')
    print(f'2021-12-01 Puzzle 1: {puzzle1(values)}')
    print(f'2021-12-01 Puzzle 2: {puzzle2(values)}')


if __name__ == '__main__':
    main()
