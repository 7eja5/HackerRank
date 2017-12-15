#!/bin/python

import sys

def simpleArraySum(n, ar):
    sum =0
    # Complete this function
    for element in ar:
        sum = element + sum
    return sum

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
