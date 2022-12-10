import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append(value)
    return data


def part1(data):
    cycle = 0
    register = 1
    signal_strength = 0
    for instruction in data:
        instruction = instruction.split(" ")
        if instruction[0] == "noop":
            cycle += 1
            signal_strength += checkCycle(cycle, register)
        else:
            to_add = int(instruction[1])
            for i in range(0, 2):
                cycle += 1
                signal_strength += checkCycle(cycle, register)
            register += to_add
    return signal_strength


def checkCycle(cycle, register):
    if (cycle - 20) % 40 == 0:
        print(cycle * register)
        return cycle * register
    return 0


def checkSprite(cycle, sprite):
    if abs(cycle - sprite) == 1 or (cycle - sprite) == 0:
        return '#'
    return '.'


def part2(data):
    cycle = -1
    sprite_position = 1
    image = [[], [], [], [], [], []]
    for instruction in data:
        instruction = instruction.split(" ")
        if instruction[0] == "noop":
            cycle += 1
            image[cycle // 40].append(checkSprite(cycle % 40, sprite_position))
        else:
            to_add = int(instruction[1])
            for i in range(0, 2):
                cycle += 1
                image[cycle // 40].append(checkSprite(cycle % 40, sprite_position))
            sprite_position += to_add
    return image


def solve(puzzle_input):
    data = parse(puzzle_input)
    sol1 = part1(data)
    sol2 = part2(data)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions[0])
    pretty_print_image(solutions[1])


def pretty_print_image(image):
    for character_list in image:
        to_print = ""
        for character in character_list:
            to_print += character
        print(to_print)


run()
