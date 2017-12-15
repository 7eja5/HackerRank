#!/bin/python

import sys

def aVeryBigSum(n, ar):
    sum=0
    # Complete this function
    for a in ar:
        sum = sum+a
        
    return sum

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
