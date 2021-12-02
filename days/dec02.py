from utils import read_input_as_str


def puzzle1(values):
    pos = {
        'horizontal': 0,
        'dept': 0
    }
    for move in values:
        match move.split():
            case ['forward', distance]:
                pos['horizontal'] += int(distance)
            case ['down', distance]:
                pos['dept'] += int(distance)
            case ['up', distance]:
                pos['dept'] -= int(distance)
    return pos['horizontal'] * pos['dept']


def puzzle2(values):
    pos = {
        'horizontal': 0,
        'dept': 0,
        'aim': 0
    }
    for move in values:
        match move.split():
            case ['forward', distance]:
                pos['horizontal'] += int(distance)
                pos['dept'] += pos['aim'] * int(distance)
            case ['down', distance]:
                pos['aim'] += int(distance)
            case ['up', distance]:
                pos['aim'] -= int(distance)
    return pos['horizontal'] * pos['dept']


def main():
    values = read_input_as_str('../data/input_dec02.txt')
    print(f'2021-12-01 Puzzle 1: {puzzle1(values)}')
    print(f'2021-12-01 Puzzle 2: {puzzle2(values)}')


if __name__ == '__main__':
    main()