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
    _fields = {f.split(':')[0]: f.split(':')[1] for f in _fields if len(f.split(':')) > 1}
    expected_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')
    valid_fields = [f for f in _fields.keys() if f in expected_fields]
    c = collections.Counter(valid_fields)

    if len(valid_fields) == len(list(set(valid_fields))) and len(valid_fields) == 8 or \
            (len(valid_fields) == 7 and 'cid' not in valid_fields):
        _key = 'hcl'
        print(f"**  {_key}: {_fields[_key]}")
        try:
            if not 1920 <= int(_fields['byr']) <= 2002:
                _key = 'byr'
                print(f"{_key}: {_fields[_key]}")
                continue
            if not 2010 <= int(_fields['iyr']) <= 2020:
                _key = 'iyr'
                print(f"{_key}: {_fields[_key]}")
                continue
            if not 2020 <= int(_fields['eyr']) <= 2030:
                _key = 'eyr'
                print(f"{_key}: {_fields[_key]}")
                continue
            if not (('cm' in _fields['hgt'] or 'in' in _fields['hgt']) and
                    (('cm' in _fields['hgt'] and 150 <= int(_fields['hgt'].replace('cm', '')) <= 193) or
                     ('in' in _fields['hgt'] and 59 <= int(_fields['hgt'].replace('in', '')) <= 76))):
                _key = 'hgt'
                print(f"{_key}: {_fields[_key]}")
                continue
            if not _fields['hcl'][0] == '#' or not len(_fields['hcl']) == 7 or not int(_fields['hcl'].replace('#', ''), 16):
                _key = 'hcl'
                print(_fields)
                print(f"{_key}: {_fields[_key]}")
                continue
            if not _fields['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                _key = 'ecl'
                print(f"{_key}: {_fields[_key]}")
                continue
            if not (len(_fields['pid']) == 9 and int(_fields['pid'].replace('0', '1'))):
                _key = 'pid'
                print(f"{_key}: {_fields[_key]}")
                continue
        except Exception as e:
            print(_fields)
            print(e)
            continue
        valid_count += 1

print(valid_count)