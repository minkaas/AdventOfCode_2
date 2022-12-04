import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        first, second = value.split(",")
        one, two = first.split("-")
        three, four = second.split("-")
        data.append([(int(one), int(two)), (int(three), int(four))])
    return data


def part1(data):
    fullycontains = 0
    for assignment in data:
        ass = assignment[0]
        ign = assignment[1]
        fullycontains = fulloverlap(ass, ign)
    return fullycontains


def part2(data):
    contains = 0
    for assignment in data:
        ass = assignment[0]
        ign = assignment[1]
        contains += overlap(ass, ign)
    return contains


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def fulloverlap(tuple1, tuple2):
    set1 = set(list(range(tuple1[0], tuple1[1]+1)))
    set2 = set(list(range(tuple2[0], tuple2[1]+1)))
    return set1.issubset(set2) or set2.issubset(set1)


def overlap(tuple1, tuple2):
    set1 = set(list(range(tuple1[0], tuple1[1]+1)))
    set2 = set(list(range(tuple2[0], tuple2[1]+1)))
    overlapset = set1.intersection(set2)
    return not len(overlapset) == 0


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
