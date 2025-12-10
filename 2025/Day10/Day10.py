import pathlib
from time import time
import pulp

def parse(puzzle_input):
    values = puzzle_input.split("\n")
    lights = []
    buttons = []
    for value in values:
        real_values = value.split(" ")
        lights.append([x for x in real_values[0] if x == '.' or x == '#'])
        temp = []
        for val in real_values[1:]:
            temp.append([int(x) for x in val if x.isdigit()])
        temp.pop(-1)
        temp.append(list(eval(real_values[-1][1:-1])))
        buttons.append(temp)
    return lights, buttons


def press_button(indicators, button):
    inds = indicators[0:len(indicators)]
    for but in button:
        inds[but] += 1
        inds[but] %= 2
    return inds


def indicator_lights_real(real_ind, pressed_ind):
    for i in range(0, len(real_ind)):
        if real_ind[i] == '.' and pressed_ind[i] == 1:
            return False
        elif real_ind[i] == '#' and pressed_ind[i] == 0:
            return False
    return True


def press_buttons(real_lights, current_lights, buttons, button_presses, lowest_button_presses):
    if button_presses >= lowest_button_presses:
        return 0
    if len(buttons) == 0 and not indicator_lights_real(real_lights, current_lights):
        return 0
    if indicator_lights_real(real_lights, current_lights):
        return button_presses
    for i in range(0, len(buttons)):
        temp_lights = press_button(current_lights, buttons[i])
        new_buttons = buttons[:]
        new_buttons.pop(i)
        button_presses_needed = press_buttons(real_lights, temp_lights, new_buttons, button_presses + 1, lowest_button_presses)
        if button_presses_needed > 0:
            lowest_button_presses = min(button_presses_needed, lowest_button_presses)
    return lowest_button_presses


def part1(lights, buttons):
    result = 0
    for machine in range(0, len(lights)):
        real_lights = lights[machine]
        possible_buttons = buttons[machine][:-1]
        current_lights = [0] * len(real_lights)
        button_presses = press_buttons(real_lights, current_lights, possible_buttons, 0, len(buttons))
        result += button_presses
        print("Done with " + str((machine / len(lights)) * 100) + "% of the button presses")
    return result


def part2(lights, buttons):
    result = 0
    for machine in range(0, len(lights)):
        supposed_lights = buttons[machine][-1]
        possible_buttons = buttons[machine][:-1]
        press_matrix = []
        for i in range(0, len(supposed_lights)):
            temp = []
            for j in range(0, len(possible_buttons)):
                if i in possible_buttons[j]:
                    temp.append(1)
                else:
                    temp.append(0)
            press_matrix.append(temp)

        # using a linear problem solver for this one
        rows = len(press_matrix)
        cols = len(press_matrix[0])
        model = pulp.LpProblem(f"machine_{machine}", pulp.LpMinimize)

        x = [pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer") for j in range(cols)]

        model += pulp.lpSum(x)
        for i in range(rows):
            model += pulp.lpSum(press_matrix[i][j] * x[j] for j in range(cols)) == supposed_lights[i]
        model.solve(pulp.PULP_CBC_CMD(msg=False))
        result += sum(v.varValue for v in x)
    return int(result)

def solve(puzzle_input):
    lights, buttons = parse(puzzle_input) # take about 130 seconds
    sol1 = part1(lights, buttons)
    lights, buttons = parse(puzzle_input)
    sol2 = part2(lights, buttons)
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("input").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()