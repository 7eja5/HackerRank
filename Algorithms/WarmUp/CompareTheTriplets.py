#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice_Score=0
    bob_Score=0
    if a0 > b0:
        alice_Score+=1
    elif a0< b0:
        bob_Score+=1
    else:
        pass
    
    if a1 > b1:
        alice_Score+=1
    elif a1< b1:
        bob_Score+=1
    else:
        pass
    
    
    if a2 > b2:
        alice_Score+=1
    elif a2< b2:
        bob_Score+=1
    else:
        pass
    
    return alice_Score,bob_Score
    
    
    
    
    # Complete this function

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


