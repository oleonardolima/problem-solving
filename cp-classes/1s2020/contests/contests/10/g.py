import math
import collections

num_tests = int(input())

dearrangements_dp = collections.defaultdict(int)
dearrangements_dp[1] = 0

for _ in range(num_tests):
    num_people = int(input())
    num_hats = num_people

    possible_cases = math.factorial(num_hats)

    for idx in range(1, num_hats + 1):
        if idx not in dearrangements_dp:
            dearrangements_dp[idx] = idx * dearrangements_dp[idx - 1] + (-1) ** idx
        continue

    favourable_cases = dearrangements_dp[num_hats]
    print("{}/{}".format(favourable_cases, possible_cases))