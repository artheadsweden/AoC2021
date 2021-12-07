from utils import read_input_as_str
from collections import defaultdict


def solver(values):
    puzzle1 = defaultdict(int)
    puzzle2 = defaultdict(int)
    for line in values:
        start, end = line.split('->')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        x1 = int(x1.strip())
        y1 = int(y1.strip())
        x2 = int(x2.strip())
        y2 = int(y2.strip())

        delta_x = x2 - x1
        delta_y = y2 - y1

        for i in range(1 + max(abs(delta_x), abs(delta_y))):
            x = x1 + (1 if delta_x > 0 else (-1 if delta_x < 0 else 0)) * i
            y = y1 + (1 if delta_y > 0 else (-1 if delta_y < 0 else 0)) * i
            if delta_x == 0 or delta_y == 0:
                puzzle1[(x, y)] += 1
            puzzle2[(x, y)] += 1

    p1 = len([k for k in puzzle1 if puzzle1[k] > 1])
    p2 = len([k for k in puzzle2 if puzzle2[k] > 1])
    return p1, p2


def main():
    values = read_input_as_str('../data/input_dec05.txt')
    p1, p2 = solver(values)
    print(f'2021-12-05 Puzzle 1: {p1}')
    print(f'2021-12-05 Puzzle 2: {p2}')


if __name__ == '__main__':
    main()
