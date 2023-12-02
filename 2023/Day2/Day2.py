import pathlib


def parse(puzzle_input):
    games = puzzle_input.split("\n")
    data = []
    for game in games:
        data.append(game.split(":")[1])  # Remove the 'Game x' part
    return data


def part1(data):
    result = 0
    for i in range(len(data)):
        game = data[i]
        if is_possible(game):
            result += i + 1
    return result


def is_possible(game):
    rounds = game.split(";")
    result = True
    for one_round in rounds:
        if result:
            cubes = one_round.split(",")
            for cube in cubes:
                number = int(cube.split(" ")[1])
                colour = cube.split(" ")[2]
                if colour == "red":
                    result = number <= 12 if result else False
                elif colour == "green":
                    result = number <= 13 if result else False
                elif colour == "blue":
                    result = number <= 14 if result else False
    return result


def part2(data):
    result = 0
    for i in range(len(data)):
        game = data[i]
        result += get_power(game)
    return result


def get_power(game):
    rounds = game.split(";")
    red = 0
    blue = 0
    green = 0
    for one_round in rounds:
        cubes = one_round.split(",")
        for cube in cubes:
            number = int(cube.split(" ")[1])
            colour = cube.split(" ")[2]
            if colour == "red":
                red = max(red, number)
            elif colour == "green":
                green = max(green, number)
            elif colour == "blue":
                blue = max(blue, number)
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
