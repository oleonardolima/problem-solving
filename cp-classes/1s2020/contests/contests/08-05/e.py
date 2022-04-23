_input = [int(num) for num in input().split(" ")]
num_sleeps = _input[0]
num_hours_day = _input[1]
sleep_time = [num for num in range(_input[2], _input[3] + 1)]

num_hours = [int(num) for num in input().split(" ")]

num_good_times = 0
curr_time = 0
for time in num_hours:
    curr_time += (time - 1)

    if curr_time > num_hours_day:
        curr_time -= num_hours_day

    print(curr_time)
    if curr_time in sleep_time:
        num_good_times += 1

print(num_good_times)
