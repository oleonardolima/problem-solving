# import math

# def longest_palindromic_contiguous(contiguous_substring):
#     start_ptr = 0
#     end_ptr = 0

#     for i in range(len(contiguous_substring)):
#         len_1 = expand_from_center(contiguous_substring, i, i)
#         len_2 = expand_from_center(contiguous_substring, i, i + 1)
#         max_len = max(len_1, len_2)

#         if max_len > (end_ptr - start_ptr):
#             start_ptr = i - math.floor((max_len - 1) / 2)
#             end_ptr = i + math.floor((max_len / 2))

#     return contiguous_substring.replace(contiguous_substring[start_ptr:end_ptr + 1], "")

# def expand_from_center(string_s, left_ptr, right_ptr):
#     if (not string_s or left_ptr > right_ptr):
#         return 0

#     while (left_ptr >= 0 and right_ptr < len(string_s) and string_s[left_ptr] == string_s[right_ptr]):
#         left_ptr -= 1
#         right_ptr += 1

#     return right_ptr - left_ptr - 1

# num_gemstones = int(input())
# gemstones_colors = "".join([str(color) for color in input().split(" ")])

# min_seconds = 0
# while gemstones_colors:
#     print(gemstones_colors)
#     gemstones_colors = longest_palindromic_contiguous(gemstones_colors)
#     min_seconds += 1


num_gemstones = int(input())
#print("num_gemstones: {}".format(num_gemstones))
gemstones_colors = "".join([str(color) for color in input().split(" ")])
#print("string_length: {}".format(len(gemstones_colors)))

# num_seconds = [[]] * (num_gemstones + 1)
# print(num_seconds)
# for idx_i in range(num_gemstones + 1):
#     for idx_j in range(num_gemstones + 1):
#         print(num_seconds[idx_i])
#         num_seconds[idx_i].append(0)

num_seconds = [[0 for x in range(num_gemstones + 1)] for y in range(num_gemstones + 1)]
#print(num_seconds[0])

for length in range(1, num_gemstones + 1):
    idx_i = 0
    idx_j = length - 1
    while idx_j < num_gemstones:
        if length == 1:
            num_seconds[idx_i][idx_j] = 1
            idx_i += 1
            idx_j += 1
            continue

        new = num_seconds[idx_i][idx_j] = 1 + num_seconds[idx_i + 1][idx_j]
        if (gemstones_colors[idx_i] == gemstones_colors[idx_i + 1]):
            num_seconds[idx_i][idx_j] = min(1 + num_seconds[idx_i + 2][idx_j], num_seconds[idx_i][idx_j])
        num_seconds[idx_i][idx_j] = min(new, num_seconds[idx_i][idx_j])

        first_occurrence = idx_i + 2
        while first_occurrence <= idx_j:
            if (gemstones_colors[idx_i] == gemstones_colors[first_occurrence]):
                new = num_seconds[idx_i + 1][first_occurrence - 1] + num_seconds[first_occurrence + 1][idx_j]
                num_seconds[idx_i][idx_j] = min(new, num_seconds[idx_i][idx_j])
            first_occurrence += 1

        idx_i += 1
        idx_j += 1

#print(num_seconds)

#print(num_seconds[0])
min_seconds = num_seconds[0][num_gemstones - 1]
print(min_seconds)