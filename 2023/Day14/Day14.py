import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    platform = []
    for value in values:
        char_list = []
        for character in value:
            if character == ".":
                char_list.append(0)
            elif character == "#":
                char_list.append(1)
            else:
                char_list.append(2)
        platform.append(char_list)
    return platform


def naive_tilting(platform):
    for i in range(len(platform[0])):
        moving_rocks = 0
        for j in range(len(platform)-1, -1, -1):
            if platform[j][i] == 2:
                moving_rocks += 1
                platform[j][i] = 0
            if platform[j][i] == 1:
                highest = j + 1
                for k in range(moving_rocks):
                    platform[highest+k][i] = 2
                moving_rocks = 0
        for k in range(moving_rocks):
            platform[k][i] = 2
    return platform


def rotate(platform):
    return [list(r) for r in zip(*platform[::-1])]


def calc_northbeams(platform):
    result = 0
    for i in range(len(platform[0])):
        column_total = 0
        row_load = len(platform)
        for j in range(len(platform)):
            if platform[j][i] == 2:
                column_total += row_load
            row_load -= 1
        result += column_total
    return result


def part1(platform):
    result = 0
    platform = naive_tilting(platform)
    result += calc_northbeams(platform)
    return result


def part2(platform):
    possibles_states = {}
    first = ""
    start_time = time()
    loop = False
    repeats = 0
    for i in range(1000):
        for j in range(4):
            # rotate and tilt 4 times
            platform = naive_tilting(platform)
            platform = rotate(platform)
        if loop and possibles_states[str(platform)] == repeats:
            return calc_northbeams(platform)
        if str(platform) not in possibles_states:
            possibles_states[str(platform)] = i
        else:
            loop = True
            repeats = 1000000000 % (len(possibles_states) - 1)
    for key in possibles_states:
        print(possibles_states[key])
    print(repeats)

    result = calc_northbeams(platform)
    return result


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def print_platform(platform):
    for plat in platform:
        print(plat)


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
