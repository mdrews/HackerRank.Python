#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    elevation = 0
    result = 0
    for x in range(n):
        if s[x] == 'U':
             elevation = elevation + 1
        else:
             elevation -= 1
        print("elevation: " + str(elevation))
        if s[x] == 'D' and elevation == -1:
            result += 1
            print("TEST")
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
