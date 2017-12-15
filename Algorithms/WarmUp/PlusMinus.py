#!/bin/python3

import sys
from decimal import Decimal

def fractionOutput(arr,n):
    positive=0
    negative=0
    zero=0
    for a in arr:
        if a >0:
            positive+=1
        elif a < 0:
            negative+=1
        else:
            zero+=1
            
    new_array_count=[positive,negative,zero]
    for ar in new_array_count:
        print(ar/n)
        

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

fractionOutput(arr,n)
