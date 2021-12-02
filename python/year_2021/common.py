import os


def read_input_lines_to_list(year: int, day: int) -> list:
    base_dir = os.getenv('ADVENT_OF_CODE_BASE')
    with open(f'{base_dir}/input/{year}/{day}/input', 'r') as f:
        lines = f.read().split('\n')[:-1]
    return lines
