import math
num_test_cases = int(input())
for test in range(num_test_cases):
    num_candies = int(input())
    if num_candies == 1 or num_candies == 2:
        print(0)
    else:
        num_ways = math.floor((num_candies - 1) / 2)
        print(num_ways)