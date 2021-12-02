import itertools


with open('input', 'r') as f:
    data = [int(d.replace('\n', '')) for d in f.readlines()]


def is_sum_of_previous(n, previous_n):
    for pairs in itertools.combinations(previous_n, 2):
        if sum(pairs) == n:
            return True
    return False

n_previous = 25
preamble = 25
for i, n in enumerate(data):
    if i < preamble:
        continue
    if not is_sum_of_previous(n, data[i-n_previous:i]):
        break

part_1_answer = n
print(f'part 1 answer: {part_1_answer}')

target_sum = part_1_answer


def find_contiguous_set(_data, _target, n=2):
    for i, d in enumerate(_data):
        if i < n:
            continue
        if sum(_data[i-n:i]) == _target:
            return _data[i-n:i]
    return None


for n in range(2, 100):
    print(n)
    found = find_contiguous_set(data, target_sum, n)
    if found is not None:
        print(found)
        print(f'sum: {min(found) + max(found)}')
        break
