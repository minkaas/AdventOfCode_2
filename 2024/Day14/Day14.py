import pathlib
import time
import re


width = 101
tall = 103


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        vals = re.findall("-?\d+,-?\d+", value)
        temp = []
        for val in vals:
            tem = val.split(",")
            temp.append((int(tem[0]), int(tem[1])))
        data.append(temp)
    return data


def part1(data):
    seconds = 100
    locations = []
    for robot in data:
        position = robot[0]
        velocity = robot[1]
        new = ((position[0] + seconds * velocity[0]) % width, (position[1] + seconds * velocity[1]) % tall)
        locations.append(new)
    quadrants = [0,0,0,0]
    for loc in locations:
        if loc[0] < width // 2:
            if loc[1] < tall // 2:
                quadrants[0] += 1
            elif loc[1] > tall // 2:
                quadrants[2] += 1
        elif loc[0] > width // 2:
            if loc[1] < tall // 2:
                quadrants[1] += 1
            elif loc[1] > tall // 2:
                quadrants[3] += 1
    average_quadrants = sum(quadrants) // len(quadrants)
    result = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    return result, average_quadrants


def neighbours(robot, locations):
    neighbour = [(0,1), (1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1)]
    for neigh in neighbour:
        bour = tuple(map(sum, zip(robot, neigh)))
        if bour in locations:
            return True
    return False

def part2(data, average):
    result = 0
    seconds = 15000
    for i in range(0, seconds):
        locations = []
        for robot in data:
            position = robot[0]
            velocity = robot[1]
            robot[0] = ((position[0] + velocity[0]) % width, (position[1] + velocity[1]) % tall)
            locations.append(robot[0])
        quadrants = [0, 0, 0, 0]
        for loc in locations:
            if loc[0] < width // 2:
                if loc[1] < tall // 2:
                    quadrants[0] += 1
                elif loc[1] > tall // 2:
                    quadrants[2] += 1
            elif loc[0] > width // 2:
                if loc[1] < tall // 2:
                    quadrants[1] += 1
                elif loc[1] > tall // 2:
                    quadrants[3] += 1
        for quad in quadrants:
            if quad > average * 2:
                print_grid(locations, i)
                return i + 1
    return result


def print_grid(locations, i):
    print("For second ", i+1, ":")
    for i in range(0, tall):
        to_print = ""
        for j in range(0 ,width):
            if (j, i) in locations:
                to_print += '█'
            else:
                to_print += '.'
        print(to_print)

def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1, average = part1(data)
    sol2 = part2(data, average)
    return sol1, sol2


def run():
    start_time = time.time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time.time() - start_time)

run()
