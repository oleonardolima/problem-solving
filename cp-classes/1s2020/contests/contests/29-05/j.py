colors = [int(color) for color in input().split(" ")]
red = colors[0]
green = colors[1]
blue = colors[2]

if red == green and green == blue:
    print(red)
else:
    max_tables = 0
    colors.sort()
    # num_balloons = 0

    while(len(colors) > 1 and sum(colors) >= 3):
        num_balloons = colors[0]
        idx_to_delete = []
        for i in range(len(colors)):
            colors[i] -= num_balloons
        print(colors)
        ptr1 = 0
        while(ptr1 < len(colors)):
            if colors[ptr1] == 0:
                colors.pop(ptr1)
            else:
                ptr1 += 1
        print(colors)
        max_tables += num_balloons

    # for i in range(len(colors)):
    #     if colors[i] == 0:
    #         continue
    #     while True:
    #         colors[i] -= 1
    #         num_balloons += 1
    #         for j in range(i + 1, len(colors)):
    #             colors[j] -= 1
    #             num_balloons += 1

    #         if num_balloons == 3:
    #             max_tables += 1
    #             num_balloons = 0

    #         if colors[i] == 0:
    #             break
    #     print(i)
    #     print(num_balloons)
    #     print(colors)
    print(max_tables)