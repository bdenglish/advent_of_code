with open('input_day_1', 'r') as f:
    data = f.readlines()

print(data)
for i, x in enumerate(data):
    for j, y in enumerate(data):
        if int(x) + int(y) == 2020:
            print(int(x) * int(y))
            break
