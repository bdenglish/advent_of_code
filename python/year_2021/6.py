from collections import Counter
import common

lines = common.read_input_lines_to_list(2021, 6)
# lines = ['3']
_state = [int(n) for n in lines[0].split(',')]


def simulate(_state, n_days):
    state_counts = Counter(_state)
    for i in range(1, n_days + 1):
        t = state_counts.copy()
        for j in range(1, 9):
            state_counts[j - 1] += state_counts[j]
            state_counts[j] = 0
        state_counts[0] -= t[0]
        state_counts[6] += t[0]
        state_counts[8] += t[0]

    # need to upgrade to 3.10 for Counter.total()
    return sum([state_counts[_n] for _n in range(9)])


print("part 1:", simulate(_state, 80))
print("part 2:", simulate(_state, 256))
