number_amount = int(input())
numbers = [int(input_) for input_ in (input().split(" "))]

idx_i = 0
idx_j = 1

different_numbers = {}
# is_even = numbers[0] % 2 == 0
# different_numbers[is_even] = [0, 1]

for idx, number in enumerate(numbers):
    is_even = number % 2 == 0
    if is_even in different_numbers:
        different_numbers[is_even] = [idx + 1, different_numbers[is_even][1] + 1]
    else:
        different_numbers[is_even] = [idx + 1, 1]
    # if (number % 2 == 0) != is_even:
    #     is_even = not is_even
    #     if is_even in different_numbers:
    #         different_numbers[is_even] = [idx + 1, different_numbers[is_even][1] + 1]
    #     else:
    #         different_numbers[is_even] = [idx + 1, 1]

# print(different_numbers)

for element in different_numbers:
    if different_numbers[element][1] == 1:
        print(different_numbers[element][0])