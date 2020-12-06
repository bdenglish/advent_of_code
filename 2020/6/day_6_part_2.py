import math
import os
import collections

advent_of_code_day = os.path.split(os.getcwd())[1]

with open(f'input_day_{advent_of_code_day}', 'r') as f:
    data = f.read()

groups = data.split('\n\n')
q_count = []
for g in groups:
    print(g)
    passengers = g.strip().split('\n')
    print(passengers)
    group_size = len(passengers)
    questions = [collections.Counter(set(list(p))) for p in passengers]
    q_total = collections.Counter()
    for q in questions:
        q_total += q
    questions_everyone_yes = [k for k, v in q_total.items() if v == group_size]
    q_count.append(len(questions_everyone_yes))

print(f'{len(groups)} groups totaling {sum(q_count)} yes')
print(q_count)
