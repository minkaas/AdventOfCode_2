import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    data = []
    for value in values:
        data.append((value))
    return data


def get_firstdig(hellp):
    index, number = find_written(hellp, True)
    other_number = 0
    for c in hellp:
        if c.isdigit():
            other_number = c
            break
    if other_number == 0:
        return number
    elif number == 0 or hellp.index(other_number) < index:
        return int(other_number)
    else:
        return number


def get_lastdig(hellp):
    index, number = find_written(hellp, False)
    hellp = hellp[::-1]
    other_number = 0
    for c in hellp:
        if c.isdigit():
            other_number = c
            break
    hellp = hellp[::-1]
    if other_number == 0:
        return number
    elif number == 0 or hellp.rindex(other_number) > index:
        return int(other_number)
    else:
        return number



def part1(data):
    result = 0
    for value in data:
        num1 = get_firstdig(value)
        num2 = get_lastdig(value)
        print(num1, num2)
        result += int(num1) * 10 + int(num2)
    return result


def part2(data):
    result = 0
    for value in data:
        num1 = get_firstdig(value)
        num2 = get_lastdig(value)
        result += int(num1) * 10 + int(num2)
    return result
    return 0


def find_written(help, first):
    if not first:
        index = 0
        number = 0
        if help.rfind('one') >= index:
            index = help.rfind('one')
            number = 1
        if help.rfind('two') >= index:
            index = help.rfind('two')
            number = 2
        if help.rfind('three') >= index:
            index = help.rfind('three')
            number = 3
        if help.rfind('four') >= index:
            index = help.rfind('four')
            number = 4
        if help.rfind('five') >= index:
            index = help.rfind('five')
            number = 5
        if help.rfind('six') >= index:
            index = help.rfind('six')
            number = 6
        if help.rfind('seven') >= index:
            index = help.rfind('seven')
            number = 7
        if help.rfind('eight') >= index:
            index = help.rfind('eight')
            number = 8
        if help.rfind('nine') >= index:
            index = help.rfind('nine')
            number = 9
        return index, number
    else:
        index = 100000
        number = 0
        if help.find('one') <= index and help.find('one') != -1:
            index = help.find('one')
            number = 1
        if help.find('two') <= index and help.find('two') != -1:
            index = help.find('two')
            number = 2
        if help.find('three') <= index and help.find('three') != -1:
            index = help.find('three')
            number = 3
        if help.find('four') <= index and help.find('four') != -1:
            index = help.find('four')
            number = 4
        if help.find('five') <= index and help.find('five') != -1:
            index = help.find('five')
            number = 5
        if help.find('six') <= index and help.find('six') != -1:
            index = help.find('six')
            number = 6
        if help.find('seven') <= index and help.find('seven') != -1:
            index = help.find('seven')
            number = 7
        if help.find('eight') <= index and help.find('eight') != -1:
            index = help.find('eight')
            number = 8
        if help.find('nine') <= index and help.find('nine') != -1:
            index = help.find('nine')
            number = 9
        return index, number



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
