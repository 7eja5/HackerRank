#!/bin/python3

import sys

def printOutput(n):
    for i in range(1,n+1):
        print((' '*(n-i))+'#'*i)

n = int(input().strip())

printOutput(n)
