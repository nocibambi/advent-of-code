# %%
from functools import reduce

# %%
with open("input_2.txt", "r") as f:
    inputs = f.read().splitlines()
# %%
# line = inputs[1]
# %%
cube_sets = {}
for line in inputs:
    cube_sets[line.split(": ")[0].split(" ")[1]] = [
        {
            cubes.split(" ")[1]: cubes.split(" ")[0]
            for cubes in cube_set.split(", ")
        }
        for cube_set in line.split(": ")[1].split("; ")
    ]

cube_sets
# %%
criteria = {"red": 12, "green": 13, "blue": 14}
# %%
# cube_set = cube_sets["1"]
# %%
possible_games = list()
for game, cube_set in cube_sets.items():
    max_color_nums = dict()
    for color in criteria.keys():
        color_max = 0
        for pull in cube_set:
            try:
                color_max = max(int(pull.get(color, "0")), color_max)
            except Exception as e:
                print(e)
                print(pull)
        max_color_nums[color] = color_max

    if all(
        [criteria[color] >= max_color_nums[color] for color in criteria.keys()]
    ):
        possible_games.append(int(game))


sum(possible_games)
# %%
powers = []
for game, cube_set in cube_sets.items():
    max_color_nums = dict()
    for color in criteria.keys():
        color_max = 0
        for pull in cube_set:
            try:
                color_max = max(int(pull.get(color, "0")), color_max)
            except Exception as e:
                print(e)
                print(pull)
        max_color_nums[color] = int(color_max)

    powers.append(reduce(lambda x, y: x * y, max_color_nums.values()))

sum(powers)
# %%
