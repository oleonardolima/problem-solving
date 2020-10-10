def reverse_num(num):
    reverse_num = 0
    while num > 0:
        reverse_num = reverse_num * 10 + num % 10
        num = num // 10

    return reverse_num

def reverse_sum(num1, num2):
    return reverse_num(reverse_num(num1) + reverse_num(num2))

num_queries = int(input())
for _ in range(num_queries):
    nums_input = [int(num) for num in input().split(" ")]
    num1 = nums_input[0]
    num2 = nums_input[1]
    print(reverse_sum(num1, num2))
