# def is_valid_pair (c_i, c_j, b_i, b_j):
#     a = b_i - c_i + 1
#     b = b_j - c_j + 1

#     if a == b:
#         return True

#     return False

num_cities = int(input())
beauty_values = [int(beauty) for beauty in input().split(" ")]

if num_cities > 1:
    for idx in range(num_cities):
        beauty_values[idx] = (beauty_values[idx], (idx + 1) - beauty_values[idx])

    beauty_values.sort(key = lambda x:x[1])
    # print(beauty_values)

    # max_sums = [el[0] for el in beauty_values]
    # valid_ptr = 0
    # for idx_i in range(num_cities):
    #     if beauty_values[idx_i][1] != beauty_values[valid_ptr][1]:
    #         valid_ptr = idx_i

    #     curr_num = beauty_values[idx_i][0]
    #     curr_diff = beauty_values[idx_i][1]

    #     for idx_j in range(valid_ptr, idx_i):
    #         other_diff = beauty_values[idx_j][1]
    #         other_num = beauty_values[idx_j][0]

    #         if other_diff != curr_diff:
    #             break

    #         if max_sums[idx_j] + curr_num >= max_sums[idx_i]:
    #             max_sums[idx_i] = max_sums[idx_j] + curr_num

    max_sums = []
    curr_sum = 0
    ptr1 = 0
    ptr2 = 1
    while ptr2 <= num_cities:
        curr_sum += beauty_values[ptr1][0]
        if ptr2 == num_cities:
            max_sums.append(curr_sum)
            curr_sum = 0
            ptr1 = ptr2
            ptr2 = ptr1 + 1
            continue
        elif beauty_values[ptr1][1] != beauty_values[ptr2][1]:
            max_sums.append(curr_sum)
            curr_sum = 0
            ptr1 = ptr2
            ptr2 = ptr1 + 1
            continue

        ptr1 += 1
        ptr2 += 1

    # print(max_sums)
    print(max(max_sums))
else:
    max_sums = beauty_values[0]
    print(max_sums)