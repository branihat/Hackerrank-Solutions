#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # Sort the array to easily calculate minimum and maximum sums
    arr.sort()

    # Calculate the minimum sum by excluding the largest element
    min_sum = sum(arr[:-1])

    # Calculate the maximum sum by excluding the smallest element
    max_sum = sum(arr[1:])

    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
