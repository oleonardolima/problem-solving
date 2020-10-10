n_queries = int(input())

for query in range(n_queries):
    input_ = [int(element) for element in input().split(" ")]
    a = input_[0]
    b = input_[1]
    c = input_[2]

    # print("\n")
    # print("a: {} b: {} c: {}".format(a, b, c))

    curr_pos = 0
    n_jumps = 0
    if a == b and c % 2 == 0:
        curr_pos = 0
    else:
        # for i in range(c):
        #     if (n_jumps) % 2 == 0:
        #         curr_pos += a
        #     else:
        #         curr_pos -= b
        #     n_jumps += 1
        #     print(curr_pos)
        if c % 2 == 0:
            curr_pos = (c // 2) * a - (c // 2) * b
        else:
            curr_pos = ((c - 1) // 2) * a - ((c - 1) // 2) * b + a
    print(curr_pos)