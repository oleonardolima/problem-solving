def is_perfect(num):
    #print(num)
    sum = 0
    while num >= 1:
        sum += num % 10
        num = num // 10

    if sum == 10:
        return True
    return False

kth_smallest = int(input())

smallest = 19
initial_num = 19
curr_k = 0
while curr_k < kth_smallest:
    if is_perfect(initial_num):
        curr_k += 1
        smallest = initial_num
    initial_num += 1

print(smallest)