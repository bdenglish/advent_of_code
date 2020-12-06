import os
import collections

advent_of_code_day = os.path.split(os.getcwd())[1]

with open(f'input_day_{advent_of_code_day}', 'r') as f:
    data = f.read()

passports = data.split('\n\n')

valid_count = 0
for _passport in passports:
    _passport = _passport.replace('\n', ' ')
    _fields = _passport.split(" ")
    _fields = [{f.split(':')[0]: f.split(':')[1]} for f in _fields if len(f.split(':')) > 1]
    expected_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')
    valid_fields = [list(f.keys())[0] for f in _fields if list(f.keys())[0] in expected_fields]
    c = collections.Counter(valid_fields)
    print(valid_fields)
    if len(valid_fields) == len(list(set(valid_fields))) and len(valid_fields) == 8 or \
        (len(valid_fields) == 7 and 'cid' not in valid_fields):
        print('valid')
        valid_count += 1

print(valid_count)