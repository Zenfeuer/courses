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

def gcd(a, b):

    if b == 0:
        return a
    
    return gcd(b, a%b)

params = [int(x) for x in input().split()]

print(gcd(params[0], params[1]))