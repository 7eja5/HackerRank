#!/bin/python3

import sys,math

def diagonal_difference(a):
    forward_Count=0
    backward_Count = 0
    for i in range(len(a)):
        forward_Count+=a[i][i]
        backward_Count+=a[(len(a)-1)-i][i]
        
    
        
    diagonal_Difference=abs(forward_Count-backward_Count)
    return diagonal_Difference

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    
#Every input must make a square matrix, that means rows ==  colums. Considering that we can make a fucntion that can work on any matrix provided that it a square


    
    
print (diagonal_difference(a))

