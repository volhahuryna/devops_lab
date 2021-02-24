input_string = input()
movement = input_string[1:3]
x = 0
y = 0
for move in movement:
    if move == 'R':
        x = x + 1
    elif move == 'L':
        x = x - 1
    elif move == 'U':
        y = y - 1
    else:
        y = y + 1
if (x == 0) and (y == 0):
    print(True)
else:
    print(False)
