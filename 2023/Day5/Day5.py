import math
import pathlib
from time import time

seeds = []
seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_hum = []
hum_to_loc = []
everything = [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_hum, hum_to_loc]

def parse(puzzle_input):
    values = puzzle_input.split("\n\n")
    values[0] = values[0].split(":")[1].strip()
    data = []
    for x in values[0].split(" "):
        seeds.append(int(x))
    for x in values[1].split("\n")[1:]:
        a, b, c = x.split(" ")
        seed_to_soil.append((int(a), int(b), int(c)))
    for x in values[2].split("\n")[1:]:
        a, b, c = x.split(" ")
        soil_to_fert.append((int(a), int(b), int(c)))
    for x in values[3].split("\n")[1:]:
        a, b, c = x.split(" ")
        fert_to_water.append((int(a), int(b), int(c)))
    for x in values[4].split("\n")[1:]:
        a, b, c = x.split(" ")
        water_to_light.append((int(a), int(b), int(c)))
    for x in values[5].split("\n")[1:]:
        a, b, c = x.split(" ")
        light_to_temp.append((int(a), int(b), int(c)))
    for x in values[6].split("\n")[1:]:
        a, b, c = x.split(" ")
        temp_to_hum.append((int(a), int(b), int(c)))
    for x in values[7].split("\n")[1:]:
        a, b, c = x.split(" ")
        hum_to_loc.append((int(a), int(b), int(c)))
    return data


def check_range(location, map):
    for x in map:
        dest, sour, rang = x
        if sour <= location <= sour + rang:
            diff = location - sour
            return dest + diff
    return location


def part1(data):
    result = 0
    here_seeds = seeds
    for the_map in everything:
        new_seeds = []
        for seed in here_seeds:
            new_seeds.append(check_range(seed, the_map))
        here_seeds = new_seeds
    here_seeds.sort()
    return here_seeds[0]


def part2(data):
    lowest = 0
    range_seeds = calculate_seeds()
    for maps in everything:
        i = 0
        while i < len(range_seeds):
            found = False
            seed_start, seed_end = range_seeds[i]
            for map_range in maps:
                destination, source, soil_range = map_range
                # Check if the start is within the range
                if source <= seed_start < (source + soil_range) and not found:
                    found = True
                    # The start will always be at least the destination and then when the source is added
                    new_start = destination + (seed_start - source)
                    # If the range of the seed extends beyond that of the map, create a new seed range
                    if seed_end < (source + soil_range):
                        range_seeds[i] = (new_start, destination + (seed_end - source))
                    else:
                        range_seeds[i] = (new_start, destination + soil_range - 1)
                        range_seeds.append((source + soil_range, seed_end))
                # Check if the end might be in the range
                elif source <= seed_end < (source + soil_range) and not found:
                    found = True
                    new_end = destination + (seed_end - source)
                    # If the start is also in the range just do it entirely, else make a new range
                    if seed_start > source:
                        range_seeds[i] = (destination + (seed_start - source), new_end)
                    else:
                        range_seeds[i] = (destination, new_end)
                        range_seeds.append((seed_start, source-1))
            i += 1
    print(range_seeds)
    result = [x for (x, y) in range_seeds]
    return min(result)


def calculate_seeds():
    result = []
    for i in range(0, len(seeds), 2):
        result.append((seeds[i], seeds[i] + seeds[i+1] - 1))
    return result


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
