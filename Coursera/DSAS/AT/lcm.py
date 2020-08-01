#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Least Common Multiple
#
# The least common multiple of two positive integers a and b is the least positive integer m that is
# divisible by both a and b.
# 
# The approach is to use GCD(a, b) to get the lcm: lcm(a, b) = a*b/GCD(a, b)
#
# Input:   integers a and b; 1 <= a,b <= 2*10^9
# Output:  lcm(a, b)

import random

# Slow solution for lcm(a, b)
def lcmNaive(a, b):
    
    minimum = a

    if b < a:
        minimum = b

    while minimum%a != 0 or minimum%b != 0:
        minimum += 1
    
    return minimum

def gcd(a, b):

    if b == 0:
        return a
    
    return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a, b)

def stressTest():

    n = int(input())

    while True:

        a = random.randint(1, n)
        b = random.randint(1, n)

        print(a, b)

        result1 = lcmNaive(a, b)
        result2 = lcm(a, b)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

params = [int(x) for x in input().split()]

#Stress Testing
#stressTest()

print(lcm(params[0], params[1]))