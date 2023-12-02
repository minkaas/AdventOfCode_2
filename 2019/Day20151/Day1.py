import pathlib
import math

def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(value)
    return data

def part1(data):
    result = 0
    for box in data:
        [l, w, h] = box.split("x")
        l = int(l)
        w = int(w)
        h = int(h)
        sides = [2*l*w, 2*w*h, 2*h*l]
        sides.sort()
        result += sum(sides) + sides[0]//2
    return result


def part2(data):
    result = 0
    for box in data:
        [l, w, h] = box.split("x")
        l = int(l)
        w = int(w)
        h = int(h)
        sides = [l, w, h]
        sides.sort()
        result += math.prod(sides) + sides[0] * 2 + sides[1] * 2
    return result


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
