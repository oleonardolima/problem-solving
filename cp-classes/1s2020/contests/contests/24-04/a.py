from sys import stdin, stdout
def calc_nth_fibonacci(n, moduloed_fibonacci, memo):
    if n == 1:
        return 1

    ptr1 = 1
    ptr2 = 1
    counter = 3
    while counter <= n:
        next_num = (ptr1 + ptr2) % moduloed_fibonacci
        ptr1 = ptr2
        ptr2 = next_num
        counter += 1

    memo[n] = ptr2
    return ptr2

memo = {}
num_test_case = int(stdin.readline())
for test in range(num_test_case):
    #nth_fibonacci = int(input())
    nth_fibonacci = int(stdin.readline())
    if nth_fibonacci not in memo:
        nth_fibonacci = calc_nth_fibonacci(nth_fibonacci, 10**8 + 7, memo)
    else:
        nth_fibonacci = memo[nth_fibonacci]
    stdout.write(str(nth_fibonacci)+'\n')