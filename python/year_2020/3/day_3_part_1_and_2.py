import functools
import math
import operator
import os


advent_of_code_day = os.path.split(os.getcwd())[1]

with open(f'input_day_{advent_of_code_day}', 'r') as f:
    data = f.readlines()


def tree_count(down, right):
    number_of_rows = len(data)
    number_of_columns = len(data[0])
    print(f'rows: {number_of_rows}')
    print(f'columns: {number_of_columns}')
    multiplier = int(right / down * number_of_rows / number_of_columns)
    print(f'multiplier: {multiplier}')

    rows = [list(d.replace('\n', '') * (multiplier + 10)) for d in data]

    def move(rows, start_coords, delta):
        print(f'moving from {start_coords} to [{start_coords[0] + delta[0]}, {start_coords[1] + delta[1]}]')
        return (rows[start_coords[0] + delta[0]][start_coords[1] + delta[1]],
                (start_coords[0] + delta[0], start_coords[1] + delta[1]))


    position = [0, 0]
    tree_count = 0

    for i in range(math.ceil(len(rows) / down - 1)):
        terrain, new_position = move(rows, position, (down, right))
        if terrain == '#':
            tree_count += 1
        position = new_position
    return tree_count


routes = [{"down": 1, "right": 1},
          {"down": 1, "right": 3},
          {"down": 1, "right": 5},
          {"down": 1, "right": 7},
          {"down": 2, "right": 1}
          ]

tree_survey = [tree_count(**r) for r in routes]
print(tree_survey)
print(functools.reduce(operator.mul, tree_survey, 1))