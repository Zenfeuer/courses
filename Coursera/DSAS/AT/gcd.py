#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Greatest Common Divisor
#
# The greatest common divisor GCD(a, b) of two non-negative integers a and b (which are not both 
# equal to 0) is the greatest integer d that divides both a and b.
# 
# GCD(a, b) = GCD(b, a'), where a' is the remainder of a/b (Euclidean algorithm)
#
# Input:   integers a and b; 1 <= a,b <= 2*10^9
# Output:  GCD(a, b)

import random

# This solution is slow, especially for large numbers, because it evaluates unnecessary cases.
def gcdNaive(a, b):

    best = 0

    for d in range(1, a+b):

        if a%d == 0 and b%d == 0:
            best = d

    return best

# This solution use the Euclidean algorithm to optimize the calculation of the GCD(a, b), where the
# premise is that the GCD(a, b) also must be the same for the reminder for a/b.
def gcd(a, b):

    if b == 0:
        return a
    
    return gcd(b, a%b)

# Stress testing that compares the results for both naive and imprived solutions.
def stressTest():

    maxNumber = int(input())

    while True:
        a = random.randint(1, maxNumber)
        b = random.randint(1, maxNumber)

        print(a, b)

        result1 = gcdNaive(a, b)
        result2 = gcd(a, b)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

#Stress testing
#stressTest()

params = [int(x) for x in input().split()]
print(gcd(params[0], params[1]))