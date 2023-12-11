import cmath
import math
import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        value = value.split(":")[1]
        result = [int(num) for num in value.split(" ") if num != ""]
        data.append(result)
    return data


def hold_boat(speed, total_time, distance):
    seconds = total_time - speed
    return seconds * speed > distance


def part1(race_data):
    result = []
    time = race_data[0]
    distance = race_data[1]
    for j in range(len(time)):
        count = 0
        for i in range(time[j]):
            if hold_boat(i, time[j], distance[j]):
                count += 1
        result.append(count)
    return math.prod(result)


def do_quadratic(a, b, c):
    d = b*b - (4 * a * c)
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    return sol1, sol2


def part2(race_data):
    time = race_data[0]
    time = int(''.join(str(e) for e in time))
    distance = race_data[1]
    distance = int(''.join(str(e) for e in distance))
    sol1, sol2 = do_quadratic(-1, time, -distance)
    return math.floor(sol1) - math.ceil(sol2) + 1


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)


run()
