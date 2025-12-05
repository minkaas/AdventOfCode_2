import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    data = []
    ranges = []
    for value in values[0].split("\n"):
        a, b = value.split("-")
        ranges.append((int(a), int(b)))
    for value in values[1].split("\n"):
        data.append(int(value))
    return ranges, data


def part1(ranges, data):
    result = 0
    for ingredient in data:
        for id_range in ranges:
            if id_range[0] <= ingredient <= id_range[1]:
                result += 1
                break
    return result


def part2(ranges):
    change = True
    while change:
        change = False
        new_range = (0, 0)
        spots = (0, 0)
        for i in range(0, len(ranges)):
            for j in range(i+1, len(ranges)):
                if change:
                    break
                range1 = ranges[i]
                range2 = ranges[j]
                if (range1[0] <= range2[0] <= range1[1]) or (range1[0] <= range2[1] <= range1[1]) or (range2[0] <= range1[0] <= range2[1]) or (range2[0] <= range1[1] <= range2[1]):
                    new_range = combine_ranges(range1, range2)
                    spots = (i, j)
                    change = True
        if change:
            ranges.pop(spots[0])
            ranges.pop(spots[1]-1)
            ranges.append(new_range)
            print(range1, range2)
            print(new_range)
    return ranges_sum(ranges)


def ranges_sum(ranges):
    result = 0
    for i in ranges:
        result += i[1] - i[0] + 1
    return result


def combine_ranges(range1, range2):
    new_range = (0, 0)
    if range1[0] < range2[0]:
        if range1[1] > range2[1]:
            return range1
        else:
            new_range = (range1[0], range2[1])
            return new_range
    elif range1[0] > range2[0]:
        if range1[1] < range2[1]:
            return range2
        else:
            new_range = (range2[0], range1[1])
            return new_range
    elif range1[0] == range2[0]:
        if range1[1] > range2[1]:
            return range1
        else:
            return range2



def solve(puzzle_input):
    ranges, data = parse(puzzle_input)
    sol1 = part1(ranges, data)
    ranges, data = parse(puzzle_input)
    sol2 = part2(ranges)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()