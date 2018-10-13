#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    counter = 0
    index = len(c)-1
    while index > 0:
        if c[index-2] == 0 and c[index-2] >= 0:
            counter += 1
            index -= 2
        else:
            index -= 1
            counter +=1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
