_input = [num for num in input().split(" ")]
num_bottles = int(_input[0])
fridge_height = int(_input[1])

bottles_heights = [int(height) for height in input().split(" ")]

bottles_heights.sort()
print(bottles_heights)

max_bottles = 0
curr_height = 0
curr_column = 0
for height in bottles_heights:
    print(height)
    if curr_height + height <= fridge_height:
        if curr_column == 1:
            curr_height += height
            curr_column = 0
        else:
            curr_height += height
            curr_column += 1
        max_bottles += 1

print(max_bottles)