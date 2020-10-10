from collections import defaultdict
_input = [int(num) for num in input().split(" ")]
l = _input[0]
r = _input[1]

if l != r:
    binary_r = bin(r)[2:]
    binary_l = bin(l)[2:].zfill(len(binary_r))

    # print(binary_l)
    # print(binary_r)

    max_idx_prefix = 0
    for idx, l_digit in enumerate(binary_l):
        if l_digit != binary_r[idx]:
            max_idx_prefix = idx
            break

    a_binary = [0 for num in range(len(binary_r))]
    a_binary[max_idx_prefix] = 0
    for idx in range(max_idx_prefix + 1, len(a_binary)):
        a_binary[idx] = 1

    b_binary = [0 for num in range(len(binary_r))]
    b_binary[max_idx_prefix] = 1

    a_binary = ''.join(str(digit) for digit in a_binary)
    b_binary = ''.join(str(digit) for digit in b_binary)

    # print(a_binary)
    # print(b_binary)

    a_binary = int(a_binary, 2)
    b_binary = int(b_binary, 2)

    max_xor = a_binary ^ b_binary

    print(max_xor)
else:
    print(l ^ r)
## first attempt
# pair_used = defaultdict(int)
# max_xor_value = 0
# for num1 in range(l, r + 1):
#     xor_value = num1 ^ num1
#     key = (num1, num1)
#     pair_used[key] += 1
#     for num2 in range(num1 + 1, r + 1):
#         key = (num1, num2)
#         pair_used[key] += 1
#         xor_value = num1 ^ num2
#         max_xor_value = max(max_xor_value, xor_value)

# print(pair_used)
# print(max_xor_value)