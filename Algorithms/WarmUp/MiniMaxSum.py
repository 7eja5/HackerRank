#!/bin/python3

import sys

def minMaxSum(arr):
    #Considering that array is small
    arr.sort()
    max = 0
    min =0
    for a in range(len(arr)-1):
        max+=arr[a]
    for ar in range(len(arr)-1,0,-1):
        min+=arr[ar]
    return str(max )+' '+ str(min)

arr = list(map(int, input().strip().split(' ')))
print (minMaxSum(arr))
