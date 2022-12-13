import pathlib


def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    data = []
    for value in values:
        value = value.split("\n")
        data.append((create_actual_list(value[0])[0], create_actual_list(value[1])[0]))
    return data


def insert_packet(result, packet):
    if len(result) == 0:
        return [packet]
    elif len(result) == 1:
        if compare_lists(result[0], packet) - 1 > 0:
            result.append(packet)
            return result
        else:
            result.insert(0, packet)
            return result
    if compare_lists(packet, result[0]) - 1 > 0:
        result.insert(0, packet)
        return result
    for i in range(0, len(result)-1):
        if compare_lists(result[i], packet) - 1 > 0 and compare_lists(packet, result[i+1]) - 1 > 0:
            result.insert(i+1, packet)
            return result
    result.append(packet)
    return result


def compare_lists(left, right):
    result = 0
    if len(left) > len(right):
        same_len = 1
    elif len(left) < len(right):
        same_len = 2
    else:
        same_len = 0
    for i in range(0, len(left)):
        if i < len(right):
            l, r = left[i], right[i]
            if type(l) is list and type(r) is list:
                result = compare_lists(l, r)
            elif type(l) is list and type(r) is int:
                r = [r]
                result = compare_lists(l, r)
            elif type(l) is int and type(r) is list:
                l = [l]
                result = compare_lists(l, r)
            elif type(l) is int and type(r) is int:
                if l == r:
                    result = 0
                elif l > r:
                    return 1
                elif l < r:
                    return 2
            if result != 0:
                return result
    if same_len and result == 0:
        return same_len
    return 0


def part1(data):
    count = 0
    for i in range(0, len(data)):
        left = data[i][0]
        right = data[i][1]
        if compare_lists(left, right) - 1 > 0:
            print(i + 1)
            count += i + 1
    return count


def create_actual_list(left_or_right):
    left_or_right = list(left_or_right)
    result = []
    open_list_counter = 1
    j = 0
    i = 0
    while i < len(left_or_right):
        i += 1
        if left_or_right[i] == '[':
            actual_list, length = create_actual_list(left_or_right[i:])
            result.append(actual_list)
            i += length
            open_list_counter += 1
        elif left_or_right[i].isdigit():
            if j <= i:
                number = left_or_right[i]
                is_number = True
                j = i
                while is_number:
                    j += 1
                    if left_or_right[j].isdigit():
                        number += left_or_right[j]
                    else:
                        is_number = False
                result.append(int(number))
        elif left_or_right[i] == ']':
            return result, i


def part2(data):
    unpacked_data = []
    for packets in data:
        unpacked_data.append(packets[0])
        unpacked_data.append(packets[1])
    sorted_packets = []
    for packet in unpacked_data:
        sorted_packets = insert_packet(sorted_packets, packet)
    sorted_packets = insert_packet(sorted_packets, [[2]])
    sorted_packets = insert_packet(sorted_packets, [[6]])
    index1, index2 = sorted_packets.index([[2]]) + 1, sorted_packets.index([[6]]) + 1
    print(sorted_packets)
    return index1 * index2


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
