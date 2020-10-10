t_cases = int(input())
for t_case in range(t_cases):
    n = int(input())
    is_x = False
    k = 2
    max_k = k
    while True:
        if 2 ** (max_k + 1) < 10 ** 9:
            max_k += 1
            continue
        break

    # print("max_k: {}".format(max_k))

    while not is_x:
        for k_i in range(k, max_k + 1):
            curr_sum = (2 ** k_i) - 1
            if n % curr_sum == 0:
                is_x = True
                break

    print(n // curr_sum)