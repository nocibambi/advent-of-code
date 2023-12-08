# %%
from functools import reduce
import re
from itertools import permutations, combinations, chain
import math as m
from pprint import pprint
from typing import Sequence
from collections import Counter, defaultdict
import os
import requests
from pprint import pprint

# %%


def get_input(day: int) -> str:
    return (
        requests.get(
            f"https://adventofcode.com/2023/day/{day}/input",
            cookies={"session": os.environ["AOC_SESSION_TOKEN"]},
        )
        .text.rstrip("\n")
        .split("\n")
    )


# %%
# !export $(cat .env)
day = 8
input = get_input(day)
input
# %%
example_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".rstrip(
    "\n"
).split(
    "\n"
)

example_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".rstrip(
    "\n"
).split(
    "\n"
)

example_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".rstrip(
    "\n"
).split(
    "\n"
)

example_1, example_2, example_3
# %%
data = input

directions = data[0]
nodes = sorted(data[2:])
dirs = directions.replace("L", "0").replace("R", "1")
nodes = {
    node.split(" = ")[0]: node.split(" = ")[1].lstrip("(").rstrip(")").split(", ")
    for node in nodes
}
# %%
node = "AAA"
steps = 0
while node != "ZZZ":
    for dir in dirs:
        node = nodes[node][int(dir)]
        steps += 1
        print(node, steps)
        if node == "ZZZ":
            break

steps
# %%
data = input

directions = data[0]
nodes = sorted(data[2:], key=lambda x: x[2])
dirs = directions  # .replace("L", "0").replace("R", "1")
nodes = {
    node.split(" = ")[0]: {
        "L": node.split(" = ")[1].lstrip("(").rstrip(")").split(", ")[0],
        "R": node.split(" = ")[1].lstrip("(").rstrip(")").split(", ")[1],
    }
    for node in nodes
}

dirs, nodes
# %%
positions = [node for node in nodes.keys() if node.endswith("A")]
steps = 0
max_steps = 1e9
while not all([pos.endswith("Z") for pos in positions]) and steps <= max_steps:
    for dir in dirs:
        positions = [nodes[pos][dir] for pos in positions]
        steps += 1
        if steps % 1e6 == 0:
            print(steps, positions)
        if all([pos.endswith("Z") for pos in positions]):
            break

steps
# %%
all([pos.endswith("Z") for pos in positions])
# %%
# total_steps = 1e7
# first_positions = [node for node in nodes.keys() if node.endswith("A")]
# steps_from_pos = defaultdict(list)
# for first_pos in first_positions:
#     print(first_pos)
#     step = 0

#     pos = first_pos
#     end = pos[-1]
#     while step <= total_steps:
#         for dir in dirs:
#             step += 1
#             pos = nodes[pos][dir]
#             end = pos[-1]

#             if step % 1e6 == 0:
#                 print(step, steps_from_pos[first_pos])

#             if end == "Z":
#                 steps_from_pos[first_pos].append(step)

# values_flat = list()
# for values in steps_from_pos.values():
#     for v in values:
#         values_flat.append(v)

# print(Counter(Counter(values_flat).values()))
# min([v for v in Counter(values_flat).values() if v >= len(first_positions)])
# %%
first_positions = [node for node in nodes.keys() if node.endswith("A")]
max_steps = 1e9
first_pos = first_positions[0]
print(first_positions, max_steps)

step = 0
pos = first_positions[0]
ending = pos[-1]
match = False


def check_match(first_pos, max_steps):
    step = 0
    pos = first_pos
    for dir in dirs:
        while step <= max_steps:
            step += 1
            pos = nodes[pos][dir]
            ending = pos[-1]

    return ending == "Z"


while not match and (step <= max_steps):
    for dir in dirs:
        step += 1
        pos = nodes[pos][dir]
        print(pos)
        ending = pos[-1]

        if ending == "Z":
            print(f"{first_pos}: {step}\n")

            for pos in first_positions[1:]:
                if not check_match(
                    first_pos=pos,
                    max_steps=step,
                ):
                    break

            print("Match!")
            match = True


check_match(first_positions[0], first_positions[1:])
# %%
