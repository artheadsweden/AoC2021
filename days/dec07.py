from utils import read_input_as_str


def solve(values, puzzle):
    max_val = max(values)
    best_moves = -1
    for goal in range(max_val):
        moves = 0
        for crab in values:
            if puzzle == 1:
                moves += abs(crab-goal)
            else:
                moves += (abs(crab-goal))*(abs(crab-goal) + 1)//2

        if best_moves < 0:
            best_moves = moves
        elif moves < best_moves:
            best_moves = moves
    return best_moves


def main():
    values = [int(x) for x in read_input_as_str('../data/input_dec07.txt')[0].split(',')]
    print(solve(values, 1))
    print(solve(values, 2))


if __name__ == '__main__':
    main()
