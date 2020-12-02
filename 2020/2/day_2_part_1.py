import re

with open('input_day_2', 'r') as f:
    data = f.readlines()

good_count = 0
for d in data:
    params = re.match('(\d+)\-(\d+)\s(\w):\s(\w+)', d)
    _min = int(params.group(1))
    _max = int(params.group(2))
    _char = params.group(3)
    _pw = params.group(4)

    matches = re.findall(_char, _pw)
    if _min <= len(matches) <= _max:
        good_count += 1

print(good_count)