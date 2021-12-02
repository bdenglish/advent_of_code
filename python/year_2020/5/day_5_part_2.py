import math
import os
import collections

advent_of_code_day = os.path.split(os.getcwd())[1]

with open(f'input_day_{advent_of_code_day}', 'r') as f:
    data = f.readlines()


def get_row(*args):
    print(args)
    c, min_row, max_row = args
    if c in ('F', 'L'):
        return min_row, math.floor(min_row + (max_row - min_row) / 2.0)
    elif c in ('B', 'R'):
        return math.ceil(min_row + (max_row - min_row) / 2.0), max_row

def get_seat_id(seat_code):
    _min_row, _max_row = (0, 127)
    position_code = seat_code[0:7]
    column_code = seat_code[7:]

    for _c in position_code:
        _min_row, _max_row = get_row(_c, _min_row, _max_row)

    row_id = _min_row
    _min_row, _max_row = (0, 7)
    for _c in column_code:
        print((_c, _min_row, _max_row))
        _min_row, _max_row = get_row(_c, _min_row, _max_row)

    seat_id = row_id * 8 + _min_row
    return seat_id


diff = set(list(range(54, 878))) - set([get_seat_id(_d.replace('\n', '')) for _d in data])
print(diff)
