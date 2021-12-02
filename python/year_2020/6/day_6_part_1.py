import math
import os
import collections

advent_of_code_day = os.path.split(os.getcwd())[1]

with open(f'input_day_{advent_of_code_day}', 'r') as f:
    data = f.read()

groups = data.split('\n\n')
print(groups[0])
q_count = []
for g in groups:
    passengers = g.strip().split('\n')
    questions = [list(p) for p in passengers]
    questions = list(set([item for sublist in questions for item in sublist]))
    print(f'{len(questions)} - {questions}')
    q_count.append(len(questions))

print(f'{len(groups)} groups totaling {sum(q_count)} yes')
print(q_count)