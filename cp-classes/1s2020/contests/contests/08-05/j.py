def is_num_good(num):
    while num > 0:
        if num % 3 == 2:
            return False
        num = num // 3
    return True

num_queries = int(input())
good_numbers = {}
for num in range(1, 2 * (10**4)):
    good_numbers[num] = is_num_good(num)

for _ in range(num_queries):
    num = int(input())
    while True:
        if good_numbers[num]:
            break
        num += 1
    # print("m: {}".format(num))
    print(num)