sum_digits = int(input())
lucky_digits = [4 ,7]

if sum_digits % lucky_digits[0] == 1:
    print(lucky_digits[0])
elif sum_digits % lucky_digits[1] == 1:
    print(lucky_digits[1])
else:
    number = []
    not_exist = False
    while sum_digits > 0:
        print(sum_digits)
        if sum_digits < 4:
            not_exist = True
            break
        else:
            while sum_digits % 4 == 0: 
                sum_digits -= 4
                number.append(4)
            while sum_digits % 7 == 0:
                sum_digits -= 7
                number.append(7)
    if not_exist:
        print(-1)
    print(number)
