import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    list1 = []
    list2 = []
    for i in range(0, len(values)):
        value = values[i].split(",")
        for direction in value:
            if i == 0:
                list1.append((direction[0], int(direction[1:])))
            else:
                list2.append((direction[0], int(direction[1:])))
    return list1, list2


def all_spots(list, result, pos):
    for direction in list:
        if (direction[0] == 'R'):
            for i in range(0, direction[1]):
                pos = (pos[0]+1, pos[1])
                result.append(pos)
        elif (direction[0] == 'L'):
            for i in range(0, direction[1]):
                pos = (pos[0]-1, pos[1])
                result.append(pos)
        elif (direction[0] == 'U'):
            for i in range(0, direction[1]):
                pos = (pos[0], pos[1]+1)
                result.append(pos)
        elif (direction[0] == 'D'):
            for i in range(0, direction[1]):
                pos = (pos[0], pos[1]-1)
                result.append(pos)
    return result


def part1(list1, list2):
    list1_spots = all_spots(list1, [], (0,0))
    list2_spots = all_spots(list2, [], (0,0))
    list1_spots, list2_spots = set(list1_spots), set(list2_spots)
    intersections = []
    for coordinate in list1_spots:
        if coordinate in list2_spots:
            intersections.append(coordinate)
    scorer = []
    for coordinate in intersections:
        scorer.append(abs(coordinate[0]) + abs(coordinate[1]))
    return min(scorer)


def part2(list1, list2):
    return 0



def solve(puzzle_input):
    list1, list2 = parse(puzzle_input)
    sol1 = part1(list1, list2)
    sol2 = part2(list1, list2)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)


run()
