from collections import defaultdict, Counter

from utils import read_input_as_str


def convert_input(values: list[int]) -> dict:
    return Counter(values)


def solver(in_dict: dict, iterations: int) -> int:
    work_dict = in_dict
    for day in range(iterations):
        worker = defaultdict(int)
        for life, cnt in work_dict.items():
            if life == 0:
                worker[6] += cnt
                worker[8] += cnt
            else:
                worker[life-1] += cnt
        work_dict = worker
    return sum(work_dict.values())


def main():
    values = convert_input([int(v) for v in read_input_as_str('../data/input_dec06.txt')[0].split(',')])
    print(f'2021-12-06 Puzzle 1: {solver(values, 80)}')
    print(f'2021-12-06 Puzzle 2: {solver(values, 256)}')


if __name__ == '__main__':
    main()