from collections import Counter
import common
import statistics
lines = common.read_input_lines_to_list(2021, 7)
lines = [int(n) for n in lines[0].split(',')]
# lines = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def part_one(lines):
    best_pos = statistics.median(lines)
    total_fuel = [abs(n - best_pos) for n in lines]
    print(statistics.median(lines))
    print(sum(total_fuel))


def part_two(lines):
    def calc_fuel(_pos, _best):
        return sum([(abs(n - _best) * (abs(n - _best) + 1)) / 2 for n in _pos])

    best_pos = int(statistics.median(lines))
    last_total_fuel = None
    for n in range(best_pos, best_pos * 4, 1):
        total_fuel = calc_fuel(lines, n)
        if last_total_fuel and total_fuel > last_total_fuel:
            print(f'got worse at {n} {last_total_fuel}')
            break
        else:
            last_total_fuel = total_fuel
            print(n)

part_one(lines)
part_two(lines)