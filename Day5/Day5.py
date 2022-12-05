import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    crates = []
    instructions = []
    instructiontime = False
    for value in values:
        if not instructiontime and value != "" and not " 1   2 " in value:
            value = [value[i:i + 4] for i in range(0, len(value), 4)]
            while len(crates) < len(value):
                crates.append([])
            for i in range(0, len(value)):
                if "[" in value[i]:
                    crates[i].insert(0, value[i])
        else:
            instructiontime = True
        if instructiontime and value != "" and not " 1   2 " in value:
            instr = [int(s) for s in value.split() if s.isdigit()]
            instructions.append(instr)
    return crates, instructions


def part1(crates, instructions):
    result = ""
    for struck in instructions:
        for i in range(0, struck[0]):
            crate = crates[struck[1]-1].pop()
            crates[struck[2]-1].append(crate)
    for stack in crates:
        result += str(stack.pop())
    return ''.join(filter(str.isupper, result))


def part2(crates, instructions):
    result = ""
    for struck in instructions:
        n_crates = crates[struck[1]-1][-struck[0]:]
        crates[struck[1]-1] = crates[struck[1]-1][:len(crates[struck[1]-1])-struck[0]]
        crates[struck[2]-1].extend(n_crates)
    for stack in crates:
        result += str(stack.pop())
    return ''.join(filter(str.isupper, result))


def solve(puzzle_input):
    crates, instructions = parse(puzzle_input)
    sol1 = part1(crates, instructions)
    crates, instructions = parse(puzzle_input)
    sol2 = part2(crates, instructions)
    return sol1, sol2


def run():
    puzzle_input = pathlib.Path("input").read_text()
    solutions = solve(puzzle_input)
    print(solutions[0])
    print(solutions[1])


run()
