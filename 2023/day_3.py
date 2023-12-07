# %%
from functools import reduce
import re
from itertools import permutations, combinations
import math as m
from pprint import pprint

# %%
with open("input_3.txt", "r") as f:
    inputs = f.read().splitlines()

inputs
# %%
symbol_list = list()
for line in inputs:
    symbols = list()
    for i, c in enumerate(line):
        symbols.append(i) if (not c.isdigit() and c != ".") else _

    symbol_list.append(symbols)

symbol_list
# %%
symbols = symbol_list[0]
symbols
# %%
i = 1
line = inputs[i]
line
# %%
part_numbers_list = list()
for i, line in enumerate(inputs):
    print(i, line)
    i = max(0, i)
    i = min(len(inputs) - 2, i)
    part_numbers = list()
    for matches in re.finditer(r"\d+", line):
        if (
            (
                any(
                    [
                        s in range(matches.start() - 1, matches.end() + 1)
                        for s in symbol_list[i - 1]
                    ]
                )
            )
            or (
                any(
                    [
                        s in range(matches.start() - 1, matches.end() + 1)
                        for s in symbol_list[i]
                    ]
                )
            )
            or (
                any(
                    [
                        s in range(matches.start() - 1, matches.end() + 1)
                        for s in symbol_list[i + 1]
                    ]
                )
            )
        ):
            part_numbers_list.append(int(matches.group()))


part_numbers_list
# %%
sum(part_numbers_list)
# %%
gear_list = list()
for line in inputs:
    gears = list()
    for i, c in enumerate(line):
        gears.append(i) if c == "*" else _

    gear_list.append(gears)

gear_list

assert len(inputs) == len(gear_list)
# %%
all_gear_vals = 0
for i, gears in enumerate(gear_list):
    print(i, gears)
    pprint(inputs[i - 1 : i + 2])
    for gear in gears:
        gear_values = list()
        for line in inputs[i - 1 : i + 2]:
            for matches in re.finditer(r"\d+", line):
                if gear in range(matches.start() - 1, matches.end() + 1):
                    gear_values.append(int(matches.group()))

        if len(gear_values) == 2:
            all_gear_vals += sum(
                [
                    gearval[0] * gearval[1]
                    for gearval in list(combinations(gear_values, r=2))
                ]
            )

all_gear_vals
# %%
list(map(lambda x, y: x * y, combinations([1, 2, 3], r=2)))
# %%
i = 138
gears = gear_list[i]
print(i, gears)
pprint(inputs[i - 1 : i + 2])
for gear in gears:
    gear_values = list()
    for line in inputs[i - 1 : i + 2]:
        for matches in re.finditer(r"\d+", line):
            if gear in range(matches.start() - 1, matches.end() + 1):
                gear_values.append(int(matches.group()))

    powers = [
        gearval[0] * gearval[1]
        for gearval in list(combinations(gear_values, r=2))
    ]

    print(gear, gear_values, powers)


# %%
