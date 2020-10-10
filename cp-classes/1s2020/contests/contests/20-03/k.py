import math
num_queries = int(input())
for query in range(num_queries):
    current_query = list(input().split(" "))
    num_book_pages = int(current_query[0])
    num_divisible = int(current_query[-1])

    sum_numbers_written = 0
    #list_ = []
    if num_book_pages >= num_divisible:
        idx_i = 1

        while idx_i % num_divisible != 0:
            idx_i += 1

        idx_j = num_book_pages

        # k = math.floor(num_book_pages / num_divisible)

        # for i in range(10):
        #     cycle_i = (num_divisible * (i + 1)) % 10
        #     sum_numbers_written += cycle_i
        # sum_numbers_written = sum_numbers_written * math.floor(k / 10)

        # for i in range(k % 10 + 1):
        #     cycle_i = (num_divisible * (i + 1)) % 10
        #     sum_numbers_written += cycle_i

        print("num book pages: {}".format(num_book_pages))
        print("initial idx_i: {}".format(idx_i))

        possible_digits = [0] * 10
        while idx_i <= num_book_pages:
            if idx_i % num_divisible != 0:
                idx_i += num_divisible
                continue
            last_digit = idx_i % 10
            possible_digits[last_digit] += 1
            idx_i += num_divisible
            #print(idx_i)

        print(possible_digits)
        for digit in range(10):
            sum_numbers_written += digit * possible_digits[digit]

        # while idx_i % num_divisible != 0:
        #     idx_i += 1

        # while idx_j % num_divisible != 0:
        #     idx_j -= 1

        # while idx_i <= idx_j:
        #     if idx_i % num_divisible == 0:
        #         if idx_i >= 10:
        #             last_digit = idx_i % 10
        #         else:
        #             last_digit = idx_i
        #         sum_numbers_written += last_digit
        #     # print(idx_i)
        #     # print(idx_j)

        #     idx_i += 1
            # if idx_i == idx_j:
            #     #print("***")
            #     if idx_i >= 10:
            #         last_digit = idx_i % 10
            #     else:
            #         last_digit = idx_i
            #     sum_numbers_written += last_digit
            #     #list_.append(idx_i)
            # else:
            #     if idx_i >= 10:
            #         last_digit = idx_i % 10
            #     else:
            #         last_digit = idx_i
            #     sum_numbers_written += last_digit
            #     #list_.append(idx_i)
            #     if idx_j >= 10:
            #         last_digit = idx_j % 10
            #     else:
            #         last_digit = idx_j
            #     sum_numbers_written += last_digit
            #     #list_.append(idx_j)

            # while idx_i % num_divisible != 0:
            #     idx_i += 1

            # while idx_j % num_divisible != 0:
            #     idx_j -= 1

    #print(sorted(list_))
    #print("\n")
    print(sum_numbers_written)