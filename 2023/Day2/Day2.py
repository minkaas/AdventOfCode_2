import pathlib
import re


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(value.split(":")[1])
    return data

def count_cubes(game):
    games = game.split(";")
    result = True
    for game in games:
        if result:
            cubes = game.split(",")
            for cube in cubes:
                if "red" in cube:
                    number = re.search(r'\d+', cube)
                    if result:
                        result = int(number.group()) <= 12
                if "green" in cube:
                    number = re.search(r'\d+', cube)
                    if result:
                        result = int(number.group()) <= 13
                if "blue" in cube:
                    number = re.search(r'\d+', cube)
                    if result:
                        result = int(number.group()) <= 14
    return result


def part1(data):
    result = 0
    for i in range(len(data)):
        game = data[i]
        if count_cubes(game):
            result += i + 1
    return result


def part2(data):
    result = 0
    for i in range(len(data)):
        game = data[i]
        result += get_power(game)
    return result


def get_power(game):
    games = game.split(";")
    red = 0
    blue = 0
    green = 0
    for game in games:
        r = 0
        b = 0
        g = 0
        cubes = game.split(",")
        for cube in cubes:
            if "red" in cube:
                number = re.search(r'\d+', cube)
                r = max(r, int(number.group()))
            if "green" in cube:
                number = re.search(r'\d+', cube)
                g = max(g, int(number.group()))
            if "blue" in cube:
                number = re.search(r'\d+', cube)
                b = max(b, int(number.group()))
        red = max(r, red)
        green = max(g, green)
        blue = max(b, blue)
    return red * green * blue


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
