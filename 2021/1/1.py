with open('input', 'r') as f:
    lines = f.readlines()
lines = [l.replace('\n', '') for l in lines]


def is_bigger_count():
    return len([(lines[n-1], line) for n, line in enumerate(lines) if n > 0 and int(line) > int(lines[n-1])])


# Part One
print(is_bigger_count(lines))

# Part Two
lines = [sum([int(lines[n-2]), int(lines[n-1]), int(line)]) for n, line in enumerate(lines) if n > 1]
print(is_bigger_count(lines))

