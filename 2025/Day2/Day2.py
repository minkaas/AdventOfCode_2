import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split(",")
    data = []
    for value in values:
        data.append(value)
    return data


def part1(IDs):
    result = 0
    for ID in IDs:
        first, last = ID.split("-")
        for i in range(int(first), int(last) + 1):
            value = str(i)
            start, finish = value[:len(value) // 2], value[len(value) // 2:]
            if start == finish:
                result += int(value)
    return result


def part2(IDs):
    result = 0
    divisors = {}
    for ID in IDs:
        first, last = ID.split("-")
        for i in range(int(first), int(last) + 1):
            value = str(i)
            if len(value) not in divisors:
                divisors[len(value)] = [x for x in range(2, len(value) + 1) if len(value) % x == 0]
            divs = divisors[len(value)]
            for j in divs:
                repeated_part = value[0:len(value) // j]
                if repeated_part * j == value:
                    result += int(value)
                    break
    return result

def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    data = parse(puzzle_input)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
