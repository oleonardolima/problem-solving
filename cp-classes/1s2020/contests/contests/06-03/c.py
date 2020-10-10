def is_unique(s):
    digits = {}
    for digit in s:
        if digit in digits:
            return False
        digits[digit] = True
    return True

input = list(input().split(" "))
l = int(input[0])
r = int(input[-1])

integer_x = -1

for i in range(l, r + 1):
    tmp_num = i
    str_num = str(tmp_num)
    if is_unique(str_num):
        integer_x = tmp_num
        break
    tmp_num = l

print(integer_x)
