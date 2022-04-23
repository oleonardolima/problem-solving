import collections
_input = [int(num) for num in input().split(" ")]
num_cells = _input[0]
cell_index = _input[1]

a_numbers = [int(num) for num in input().split(" ")]

portals = [num for num in range(1, num_cells)]

transportation_system = collections.defaultdict(int)

for portal in portals:
    transportation_system[portal] = portal + a_numbers[portal - 1]
#print(transportation_system)

is_possible = False
cell = 1
while cell in transportation_system:
    if cell == cell_index or transportation_system[cell] == cell_index:
        is_possible = True
        break
    elif cell > cell_index:
        break
    cell = transportation_system[cell]


if is_possible:
    print("YES")
else:
    print("NO")