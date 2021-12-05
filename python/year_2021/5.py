
import common

def get_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    dx = x2 - x1
    dy = y2 - y1
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    if swapped:
        points.reverse()
    return points


def plot(lines, diagonals):
    overlap = dict()
    for s in lines:
        p = [int(i) for i in s.replace(" -> ", ",").split(",")]
        if not (p[0] == p[2] or p[1] == p[3]):
            if not diagonals:
                continue
        for k in get_line(*p):
            overlap[k] = 1 if k not in overlap else overlap[k] + 1
    return len([1 for n in overlap.values() if n > 1])


lines = common.read_input_lines_to_list(2021, 5)

print("part 1:", plot(lines, False))
print("part 2:", plot(lines, True))