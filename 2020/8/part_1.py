
with open('input', 'r') as f:
    data = [d.replace('\n', '') for d in f.readlines()]

traveled = set()
jumps = [i for i, v in enumerate(data) if 'jmp' in v]
print(jumps)
for j in jumps:
    accumulator = 0
    next_move = 0
    traveled = set()
    while next_move not in traveled:
        traveled.add(next_move)
        if next_move >= len(data):
            break
        _next_command = data[next_move]
        if next_move == j:
            print(f'replacing {j}')
            _next_command = 'nop 0'
        if 'nop' in _next_command:
            next_move += 1
        elif 'acc' in _next_command:
            acc = _next_command.replace('acc ', '')
            if '-' in acc:
                accumulator -= int(acc.replace('-', ''))
            else:
                accumulator += int(acc.replace('+', ''))
            next_move += 1
        elif 'jmp' in _next_command:
            jump = _next_command.replace('jmp ', '')
            if '-' in jump:
                next_move -= int(jump.replace('-', ''))
            else:
                next_move += int(jump.replace('+', ''))
    print(next_move, accumulator)
    if next_move >= len(data):
        print(f'answer: {accumulator}')
        break