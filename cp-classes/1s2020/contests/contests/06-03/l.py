def reverse_substring(s, ptr1, ptr2):
    #print("*")
    while ptr1 < ptr2:
        s[ptr1], s[ptr2] = s[ptr2], s[ptr1]
        ptr1 += 1
        ptr2 -= 1
    #print("**")
    return s

num_test_cases = int(input())
for test_case in range(num_test_cases):
    str_len = int(input())
    test = [char for char in input()]
    n = str_len
    #print(n)
    smallest_s = "".join(test)
    smallest_k = n + 1
    for k in range(1, n + 1):
        #print("k: {}".format(k))
        for i in range(0, n - k + 1):
            #print("i: {}".format(i))
            reversed_string = "".join(reverse_substring(test, i, (i + k - 1)))
            #print(reversed_string)
            if reversed_string <= smallest_s:
                if reversed_string != smallest_s:
                smallest_s = reversed_string
                if k < smallest_k:
                   smallest_k = k

    print("\n")
    print(smallest_s)
    print(smallest_k)
