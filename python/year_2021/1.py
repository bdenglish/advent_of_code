import os


base_dir = os.getenv('ADVENT_OF_CODE_BASE')
with open(f'{base_dir}/input/2021/1/input', 'r') as f:
    lines = f.read().split('\n')[:-1]


def is_bigger_count(lines):
    return len([(lines[n-1], line) for n, line in enumerate(lines) if n > 0 and int(line) > int(lines[n-1])])


# Part One
print(is_bigger_count(lines))

# Part Two
lines = [sum([int(lines[n-2]), int(lines[n-1]), int(line)]) for n, line in enumerate(lines) if n > 1]
print(is_bigger_count(lines))

