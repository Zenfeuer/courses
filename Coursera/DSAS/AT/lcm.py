#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Least Common Multiple
#
# The least common multiple of two positive integers a and b is the least positive integer m that is
# divisible by both a and b.
# 
# lcm(a, b) = a*b/GCD(a, b)
#
# Input:   integers a and b; 1 <= a,b <= 2*10^9
# Output:  lcm(a, b)

def gcd(a, b):

    if b == 0:
        return a
    
    return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a, b)

params = [int(x) for x in input().split()]

print(lcm(params[0], params[1]))