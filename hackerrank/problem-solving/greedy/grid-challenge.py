# Problem Statement: https://www.hackerrank.com/rest/contests/master/challenges/grid-challenge/download_pdf?language=English

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    is_ascending = True

    print(grid)

    for i, row in enumerate(grid):
        grid[i] = sorted(row)
    
    print(grid)

    n_elements = len(grid)

    
    for col in range(len(grid[0])):
        print("col", col)
        
        last_element = grid[0][col]
        
        for row in range(len(grid)):

            print(grid[row][col])

            if grid[row][col] < last_element:
                is_ascending = False
                break

            last_element = grid[row][col]

        if not is_ascending:
            break

    if is_ascending:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
