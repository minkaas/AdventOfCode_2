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

# 0 is north, 1 is south, 2 is -> east, 3 is <- west
def tilt(platform, direction):
    down = True if direction == 1 or direction == 2 else False
    trans = True if direction == 2 or direction == 3 else False
    platform = transpose(platform) if trans else platform
    result = 0
    if not down: # north
        for i in range(len(platform[0])):
            column_total = 0
            moving_rocks = 0
            row_load = 0
            for j in range(len(platform)-1, -1, -1):
                if platform[j][i] == 2:
                    moving_rocks += 1
                if platform[j][i] == 1:
                    for k in range(moving_rocks):
                        column_total += row_load - k
                    moving_rocks = 0
                row_load += 1
            for k in range(moving_rocks):
                column_total += row_load - k
            result += column_total
    if down:
        for i in range(len(platform[0])):
            column_total = 0
            moving_rocks = 0
            row_load = len(platform)
            for j in range(0, len(platform), 1):
                if platform[j][i] == 2:
                    moving_rocks += 1
                if platform[j][i] == 1:
                    for k in range(moving_rocks):
                        column_total += row_load + k
                    moving_rocks = 0
                row_load -= 1
            result += column_total
    return result


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

def transpose(matrix):
    return list(map(list, zip(*matrix)))


def part1(platform):
    result = 0
    platform = naive_tilting(platform)
    result += calc_northbeams(platform)
    return result

# 0 is north, 1 is south, 2 is -> east, 3 is <- west

def part2(platform):
    possibles_states = {}
    first = ""
    start_time = time()
    loop = False
    repeats = 0
    for i in range(1000):
        for j in range(4):
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
