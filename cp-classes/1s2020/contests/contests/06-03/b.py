n_commands = input()
commands = input()

possible_pos =  []

# successfully
pos = 0
for command in commands:
    if command == 'L':
        pos -= 1
    else:
        pos += 1

possible_pos.append(pos)

# only left
pos = 0
for command in commands:
    if command == 'L':
        pos -= 1

possible_pos.append(pos)

# only right
pos = 0
for command in commands:
    if command == 'R':
        pos += 1

possible_pos.append(pos)

max = 0
min = 0

for pos in possible_pos:
    if pos > max:
        max = pos
    if pos < min:
        min = pos

total = 0
for i in range(min, max+1):
    total += 1

print(total)
