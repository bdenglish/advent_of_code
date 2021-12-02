import common


lines = common.read_input_lines_to_list(2021, 2)

h = 0
d = 0

for line in lines:
    cmd, dist = line.split()
    if cmd == "forward":
        h += int(dist)
    elif cmd == "down":
        d += int(dist)
    elif cmd == "up":
        d -= int(dist)

print(h * d)

h = 0
d = 0
aim = 0

for line in lines:
    cmd, dist = line.split()
    dist = int(dist)
    if cmd == "forward":
        h += dist
        d = d + (aim * dist)
    elif cmd == "down":
        aim += dist
    elif cmd == "up":
        aim -= dist
    print(f'cmd: {cmd}, dist: {dist}')
    print(f'h: {h}, d: {d}, aim: {aim}')
    print('-')

print(h * d)