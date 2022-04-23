from collections import deque, defaultdict
num_snacks = int(input())
snacks = deque([int(num) for num in input().split(" ")])

other_sizes = defaultdict(bool)
while snacks:
    sizes_to_print = []
    if snacks:
        current_size = snacks.popleft()

    #print(current_size)
    if current_size == num_snacks:
        num_snacks -= 1
        sizes_to_print.append(current_size)

        while other_sizes[num_snacks]:
            if other_sizes[num_snacks] == True:
                sizes_to_print.append(num_snacks)
                num_snacks -= 1
                continue

        # for other_size in other_sizes:
        #     if other_size == num_snacks:
        #         num_snacks -= 1
        #         sizes_to_print.append(other_size)
        #         other_sizes.remove(other_size)
        #         continue
        #     break

        # if other_sizes:
        #     for size in sizes_to_print[1:]:
        #         other_sizes.remove(size)

        print(*sizes_to_print)
        continue

    other_sizes[current_size] = True
    print()
