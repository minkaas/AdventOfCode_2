import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        value = value.split("->")
        coordinates = []
        for coordinate in value:
            coordinate = coordinate.split(",")
            coordinates.append((int(coordinate[0]), int(coordinate[1])))
        data.append(coordinates)
    covered = []
    for path in data:
        for i in range(1, len(path)):
            if path[i-1][0] - path[i][0] > 0:
                for j in range(path[i][0], path[i-1][0]+1):
                    covered.append((j, path[i][1]))
            elif path[i-1][0] - path[i][0] < 0:
                for j in range(path[i-1][0], path[i][0]+1):
                    covered.append((j, path[i][1]))
            elif path[i-1][1] - path[i][1] > 0:
                for j in range(path[i][1], path[i-1][1]+1):
                    covered.append((path[i][0], j))
            else:
                for j in range(path[i-1][1], path[i][1]+1):
                    covered.append((path[i][0], j))
        covered.append(path[len(path)-1])
    covered = list(set(covered))
    return covered


def part1(covered):
    endless = False
    units = 0
    while not endless:
        covered = new_sand_grain(covered)
        if not covered:
            endless = True
        else:
            units += 1
    return units


def new_sand_grain(covered):
    new_sand_pos = (500, 0)
    highest_x = 0
    for coords in covered:
        highest_x = max(highest_x, coords[1])
    on_something = False
    while not on_something:
        sand_y = new_sand_pos[0]
        sand_x = new_sand_pos[1]
        if (sand_y, sand_x+1) in covered:                 # is it on top of something
            on_something = True
            if (sand_y-1, sand_x+1) in covered:           # is left diagonally free
                if (sand_y+1, sand_x+1) in covered:       # is right diagonally free
                    covered.append(new_sand_pos)          # if both are not free, just keep it where it is
                else:
                    new_sand_pos = (sand_y+1, sand_x+1)   # sand goes to the right
                    on_something = False
            else:
                new_sand_pos = (sand_y-1, sand_x+1)       # sand goes to the left
                on_something = False
        else:
            new_sand_pos = (sand_y, sand_x+1)
            if sand_x + 1 >= highest_x:
                return 0
    return covered




def part2(covered):
    blocked = False
    highest_x = 0
    for coords in covered:
        highest_x = max(highest_x, coords[1])
    for i in range(0, 1000):
        covered.append((i, highest_x+2))
    units = 0
    while not blocked:
        covered = new_sand_grain(covered)
        if (500, 0) in covered:
            blocked = True
        units += 1
        if units % 100 == 0:
            print(units)
    return units

def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    data = parse(puzzle_input)
    sol2 = part2(data)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
