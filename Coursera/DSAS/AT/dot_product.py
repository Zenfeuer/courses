#!/bin/python3
# @author: Darwing Hernandez <darwinghga@gmail.com>

# Maximizing Dot Product
#
# Input:    
# Output:   

import random

def dotProduct(A, B, n):

    i = 0
    maxProduct = 0

    for i in range(n):
        maxProduct += A[i]*B[i]
    
    return maxProduct

# Stress testing both solutions
#TODO

n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

# Stress testing
#stressTest(n)

A = sorted(A)
B = sorted(B)

# Call fast solution
print(dotProduct(A, B, n))