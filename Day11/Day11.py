import pathlib


class Monkey:
    def __init__(self, items, operation, opamount, divamount, true, false):
        self.items = items
        self.operation = operation
        self.opamount = opamount
        self.divamount = divamount
        self.true = true
        self.false = false
        self.activity = 0

    def monk_print(self):
        print("Monkey: " + str(self.items))

def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    monkeys = []
    for value in values:
        value = value.split("\n")
        items = [int(s) for s in value[1].split(":")[1].split(",")]
        if "old * old" in value[2]:
            operation = '^'
            opamount = 2
        else:
            operation = '*' if '*' in value[2] else '+'
            opamount = [int(s) for s in value[2].split() if s.isdigit()][0]
        divamount = [int(s) for s in value[3].split() if s.isdigit()][0]
        true_val = [int(s) for s in value[4].split() if s.isdigit()][0]
        false_val = [int(s) for s in value[5].split() if s.isdigit()][0]
        monkeys.append(Monkey(items, operation, opamount, divamount, true_val, false_val))
    return monkeys


def do_monkey(erjan, monkeys, part2 = False):
    while len(erjan.items) != 0:
        item = erjan.items.pop(0)
        erjan.activity += 1
        if erjan.operation == '*':
            worry_level = item * erjan.opamount
        elif erjan.operation == '+':
            worry_level = item + erjan.opamount
        else:
            worry_level = item * item
        if not part2:
            worry_level = worry_level // 3
        if worry_level % erjan.divamount == 0:
            monkeys[erjan.true].items.append(worry_level)
        else:
            monkeys[erjan.false].items.append(worry_level)
    return monkeys



def part1(data):
    activities = []
    result = []
    for i in range(0, 20):
        for monk in data:
            result = do_monkey(monk, data)
    for monk in result:
        activities.append(monk.activity)
    activities.sort()
    return activities.pop() * activities.pop()


def part2(data):
    activities = []
    result = []
    for i in range(0, 10000):
        for monk in data:
            result = do_monkey(monk, data, True)
        if i % 100 == 0:
            print("Done with round " + str(i))
    for monk in result:
        activities.append(monk.activity)
    activities.sort()
    return activities.pop() * activities.pop()

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