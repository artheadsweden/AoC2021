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

def puzzle2(values):
    gamma, epsilon = gamma_epsilon_str(values)
    new_values_oxygen = values.copy()
    pos = 0
    while len(new_values_oxygen) > 1:
        new_values_oxygen = [g for g in new_values_oxygen if g[pos] == gamma[pos]]
        pos += 1
    new_values_co2 = values.copy()
    pos = 0
    while len(new_values_co2) > 1:
        new_values_co2 = [e for e in new_values_co2 if e[pos] == epsilon[pos]]
        pos += 1
    oxygen = new_values_oxygen[0]
    co2 = new_values_co2[0]
    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)
    return oxygen * co2

def puzzle1(values):
    gamma, epsilon = gamma_epsilon_str(values)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def main():
    values = read_input_as_str('../data/input_dec03.txt')
    print(puzzle1(values))
    print(puzzle2(values))

if __name__ == '__main__':
    main()