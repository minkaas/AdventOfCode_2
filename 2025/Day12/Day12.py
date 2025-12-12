import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    presents = []
    tree_regions = []
    cur_present = []
    for value in values[0].split("\n"):
        if value[0].isdigit() and value[0] != '0':
            presents.append(cur_present)
            cur_present = []
            continue
        elif '.' in value or '#' in value:
            cur_present.append([0 if x == '.' else 1 for x in value])
    presents.append(cur_present)
    for value in values[1].split("\n"):
        shape, quantities = value.split(":")
        quantities = [int(x) for x in quantities.split()]
        tree_regions.append((shape, quantities))
    return presents, tree_regions


def part1(presents, tree_regions):
    result = 0
    for region in tree_regions:
        region_size = region[0].split("x")
        max_tiles = int(region_size[0]) * int(region_size[1]) // 2
        black_tiles = 0
        white_tiles = 0
        for quantity in range(0, len(region[1])):
            present_quantity = region[1][quantity]
            p = presents[quantity]
            covering1, covering2 = p[0][0] + p[0][2] + p[1][1] + p[2][0] + p[0][0], p[0][1] + p[1][0] + p[1][2] + p[2][1]
            if covering1 == covering2:
                black_tiles += covering1 * present_quantity
                white_tiles += covering2 * present_quantity
            elif covering1 > covering2:
                for i in range(0, present_quantity):
                    if black_tiles < white_tiles:
                        white_tiles += covering2
                        black_tiles += covering1
                    else:
                        white_tiles += covering1
                        black_tiles += covering2
            elif covering2 > covering1:
                for i in range(0, present_quantity):
                    if black_tiles < white_tiles:
                        white_tiles += covering1
                        black_tiles += covering2
                    else:
                        white_tiles += covering2
                        black_tiles += covering1
        if white_tiles < max_tiles and black_tiles < max_tiles:
            result += 1
    return result


def solve(puzzle_input):
    presents, tree_regions = parse(puzzle_input)
    sol1 = part1(presents, tree_regions)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()
