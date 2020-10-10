# Problem Statement: https://www.hackerrank.com/rest/contests/master/challenges/ctci-ransom-note/download_pdf?language=English

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_map = defaultdict(int)
    
    for word in magazine:
        magazine_map[word] += 1
    
    for word in note:
        if word not in magazine_map:
            return "No"
        elif magazine_map[word] == 0:
            return "No"
        else:
            magazine_map[word] -= 1
    
    return "Yes"
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
