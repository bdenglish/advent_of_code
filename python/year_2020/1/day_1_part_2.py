import sys


with open('input_day_1', 'r') as f:
    data = f.readlines()

for i, x in enumerate(data):
    for j, y in enumerate(data):
        for k, z in enumerate(data):
            if int(x) + int(y) + int(z) == 2020 and x != y and y!= z and x != z:
                print(int(x) * int(y) * int(z))
                print(x, y, z)
                sys.exit()
