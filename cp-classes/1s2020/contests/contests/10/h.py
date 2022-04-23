digits = [int(digit) for digit in input()]
print(digits)
num_digits = len(digits)
if num_digits > 1:
    has_zero = False
    has_one = False
    for digit in digits:
        if digit == 0:
            has_zero = True
        elif digit == 1:
            has_one = True

    ptr1 = num_digits
    ptr2 = ptr1 - 1

    while ptr2 >=0:
        sub = 0
        if digits[ptr1] == 0:
            sub = -1
            digits[ptr1] = 9
            



    pass
else:
    max_product = "".join(str(digit) for digit in digits)
    print(max_product)