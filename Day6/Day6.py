import pathlib


def parse(puzzle_input):
    data = list(puzzle_input)
    return data


def part1(data):
    for i in range(0, len(data)-4):
        signal = data[i:i+4]
        if len(set(signal)) == 4:
            return i+4
    return 0


def part2(data):
    for i in range(0, len(data)-14):
        signal = data[i:i+14]
        signal = set(signal)
        if (len(set(signal))) == 14:
            return i+14
    return 0


def one_liner(n):
    return [i+n for i in range(0, len(list(pathlib.Path("input").read_text().strip()))) if len(set(list(pathlib.Path("input").read_text().strip())[i:i+n])) == n][0]

def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = one_liner(4)
    sol2 = one_liner(14)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()