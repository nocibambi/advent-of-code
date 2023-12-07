# %%
from functools import reduce
import re
from itertools import permutations, combinations
import math as m
from pprint import pprint
from typing import Sequence
from collections import Counter


# %%
def clean_seq(string: Sequence[str], sep=" "):
    return [s.strip() for s in string.split(" ") if s]


# %%
with open("input_5.txt", "r") as f:
    inputs = f.read().rstrip("\n")
inputs.split("\n\n")

with open("input_5_ex.txt", "r") as f:
    inputs = f.read().rstrip("\n")
inputs.split("\n\n")
# %%
seeds = list(map(int, inputs.split("\n\n")[0].split(": ")[1].split(" ")))
seeds
# %%
# seeds_to_soil = inputs.split("\n\n")[1].split(":\n")[1].split("\n")
# seeds_to_soil
# %%
# seed = seeds[1]

seeds_vals = [[s] for s in seeds]
for code_map in inputs.split("\n\n")[1:]:
    print(code_map.split(":\n")[0])
    code_map = code_map.split(":\n")[1].split("\n")
    for i in range(len(seeds)):
        seed = seeds_vals[i][-1]
        print(seed)
        seeds_vals[i].append(seed)
        for line in code_map:
            vals = list(map(int, line.split(" ")))
            print(
                seed >= vals[1] and seed <= vals[1] + vals[2],
                vals[0],
                vals[1],
                vals[2],
            )
            if seed >= vals[1] and seed <= vals[1] + vals[2]:
                seeds_vals[i][-1] = seed + (vals[0] - vals[1])
                print(seeds_vals[i])
                break

# True 391285622 257757572 195552540
# [364807853, 498335903]
seeds_vals
# %%
min([vals[-1] for vals in seeds_vals])
# [vals[-1] for vals in seeds_vals]
# %%
seeds = list(map(int, inputs.split("\n\n")[0].split(": ")[1].split(" ")))
seed_ranges = {seeds[i * 2]: seeds[i * 2 + 1] for i in range(len(seeds) // 2)}
# %%
# seeds_vals = [[s] for s in seeds]
for seed_range_min in sorted(seed_ranges.keys()):
    seed_range_max = seed_ranges[seed_range_min]
    print(seed_range_min, seed_range_max)
    for code_map in inputs.split("\n\n")[1:]:
        print(code_map.split(":\n")[0])
        code_map = code_map.split(":\n")[1].split("\n")
        for line in code_map:
            vals = list(map(int, line.split(" ")))
            dest, source,   vals[0],vals[1],vals[2],
            print(
                vals[0],
                vals[1],
                vals[2],
                seed_range_min >= vals[1]
                and seed_range_max <= vals[1] + vals[2],
            )

        # for i in range(len(seeds)):
        #     seed = seeds_vals[i][-1]
        #     print(seed)
        #     seeds_vals[i].append(seed)
        #         if seed >= vals[1] and seed <= vals[1] + vals[2]:
        #             seeds_vals[i][-1] = seed + (vals[0] - vals[1])
        #             print(seeds_vals[i])
        #             break

    print()

# %%
