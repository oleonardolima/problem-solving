num_days = int(input())
days = [int(num) for num in input().split(" ")]

max_len = 1
curr_len = 1
for i in range(1, len(days)):
    num = days[i]
    other_num = days[i - 1]
    if num >= other_num:
        curr_len += 1
    else:
        max_len = max(max_len, curr_len)
        curr_len = 1

    max_len = max(max_len, curr_len)
print(max_len)

