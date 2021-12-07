from utils import read_input_as_str
from collections import Counter


def gamma_epsilon_str(values):
    cols = list(zip(*values[::-1]))
    cols = [col[::-1] for col in cols]
    gamma = ''
    for r in cols:
        counter = Counter(r)
        gamma += counter.most_common(1)[0][0]
    epsilon = ''.join('0' if d == '1' else '1' for d in gamma)
    return gamma, epsilon


def bit_counts(in_data, pos):
    return len(list(filter(lambda x: x[pos] == '1', in_data)))


def filter_candidates(f, candidates):
    n = 0
    while len(candidates) > 1:
        if f(bit_counts(candidates, n) * 2, len(candidates)):
            candidates = list(filter(lambda x: x[n] == '1', candidates))
        else:
            candidates = list(filter(lambda x: x[n] == '0', candidates))
        n += 1

    return int(candidates[0], 2)


def puzzle2(values):
    oxygen = filter_candidates(lambda a, b: a >= b, values)
    co2 = filter_candidates(lambda a, b: a < b, values)
    return oxygen * co2


def puzzle1(values):
    gamma, epsilon = gamma_epsilon_str(values)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def main():
    values = read_input_as_str('../data/input_dec03.txt')
    print(f'2021-12-03 Puzzle 1: {puzzle1(values)}')
    print(f'2021-12-03 Puzzle 2: {puzzle2(values)}')


if __name__ == '__main__':
    main()
