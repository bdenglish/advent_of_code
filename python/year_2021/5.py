import re

import numpy as np
import pandas as pd

import common

lines = common.read_input_lines_to_list(2021, 5)

# lines = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1',
#          '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4',
#          '0,0 -> 8,8', '5,5 -> 8,2']


rows = []
for line in lines:
    coords = re.split(' -> ', line)
    x1 = coords[0].split(',')[0]
    y1 = coords[0].split(',')[1]
    x2 = coords[1].split(',')[0]
    y2 = coords[1].split(',')[1]
    rows.append({'x1': int(x1), 'y1': int(y1), 'x2': int(x2), 'y2': int(y2)})

df = pd.DataFrame(rows)
print(df)
mins = df.min()
maxs = df.max()
max_x = max(maxs['x1'], maxs['x2'], maxs['y1'], maxs['y2'])
max_y = max_x

vent_map = []
vent_map_row = [0 for _ in range(max_y + 1)]

for r in range(max_x + 1):
    vent_map.append(vent_map_row)

vent_matrix = np.matrix(vent_map)
for r in rows:
    # if r['x2'] == 2 and r['y2'] == 0:
    #     print(r)
    if r['x1'] == r['x2']:
        # vertical
        start = min(r['y1'], r['y2'])
        end = max(r['y1'], r['y2']) + 1
        for n in range(start, end, 1):
            vent_matrix[n, r['x1']] = vent_matrix[n, r['x1']] + 1
    elif r['y1'] == r['y2']:
        # horizontal
        start = min(r['x1'], r['x2'])
        end = max(r['x1'], r['x2']) + 1
        for n in range(start, end, 1):
            vent_matrix[r['y1'], n] = vent_matrix[r['y1'], n] + 1
    else:
        print(r)
        x = r['x1']
        y = r['y1']
        if x > y and y < r['y2']:
            while y <= r['y2']:
                vent_matrix[y, x] = vent_matrix[y, x] + 1
                x -= 1
                y += 1
        elif x < y:
            while x <= r['x2']:
                vent_matrix[y, x] = vent_matrix[y, x] + 1
                x += 1
                y -= 1
        else:
            if x < r['x2']:
                y_s = y
                while x <= r['x2']:
                    vent_matrix[y, x] = vent_matrix[y, x] + 1
                    x += 1
                    if y_s <= r['y2']:
                        y += 1
                    else:
                        y -= 1
            else:
                x = r['x2']
                y = r['y2']
                y_s = y
                while x <= r['x1']:
                    vent_matrix[y, x] = vent_matrix[y, x] + 1
                    x += 1
                    if y_s <= r['y1']:
                        y += 1
                    else:
                        y -= 1

# print(vent_matrix)

print(len(np.where(vent_matrix > 1)[0]))
