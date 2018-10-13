#!/bin/python3
from collections import defaultdict
import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = defaultdict(lambda: 0)
    result = 0
    for x in range(n):
        pairs[ar[x]] += 1
    for y in pairs:
        result += pairs[y] // 2
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
