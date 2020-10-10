def is_equivalent(str_a, str_b):
    if len(str_a) % 2 != 0 or len(str_b) % 2 != 0:
        if str_a == str_b:
            return True
        return False
    elif str_a == str_b:
        return True
    else:
        len_a = len(str_a)
        len_b = len(str_b)

        a1_i, a1_j = 0, (len_a // 2)
        a2_i, a2_j = (len_a // 2), (len_a)

        b1_i, b1_j = 0, (len_b // 2)
        b2_i, b2_j = (len_b // 2), (len_b)

        a1 = str_a[a1_i:a1_j]
        a2 = str_a[a2_i:a2_j]

        b1 = str_b[b1_i:b1_j]
        b2 = str_b[b2_i:b2_j]

        # print(a2_i)
        # print(a2_j)
        # print("a1: {} | a2: {}".format(a1, a2))
        # print("b1: {} | b2: {}".format(b1, b2))

        if is_equivalent(a1, b1) and is_equivalent(a2, b2):
            return True
        elif is_equivalent(a1, b2) and is_equivalent(a2, b1):
            return True
    return False

str_a = [el for el in input()]
str_b = [el for el in input()]

if is_equivalent(str_a, str_b):
    print("YES")
else:
    print("NO")