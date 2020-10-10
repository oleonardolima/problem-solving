# Problem Statement: https://www.hackerrank.com/rest/contests/master/challenges/minimum-absolute-difference-in-an-array/download_pdf?language=English

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr, n):
    """ Not Greedy Algorithm -> Runtime Error ~ O(n²)
    n_elements = n
    elements = (sorted(arr)).copy()

    abs_diff = math.inf
     for i, n_i in enumerate(elements):
        for n_j in (elements[i+1:]):
            diff_value = n_i - n_j
            if abs(diff_value) < abs_diff:
                abs_diff = abs(diff_value)
            print("{} - {}".format(n_i, n_j))
            print(diff_value)
            print(abs_diff)
    return abs_diff
    """
    # Greedy Algorithm ~O(n*log(n)) -> It depends of the sorting time
    n_elements = n
    elements = (sorted(arr)).copy() # Assuming O(n*log(n)) ~ MERGE-SORT
    
    # Greedy Choice -> First Minimum Absolute Difference
    abs_diff = abs(elements[0] - elements[1])

    elements = elements[1:]
    n_elements = n - 2

    for idx in range(n_elements): # O(n)
        print(idx)
        diff_value = elements[idx] - elements[idx+1]
        if (abs(diff_value) < abs_diff):
            abs_diff = abs(diff_value)

    return abs_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
