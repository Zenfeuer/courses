#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Pairwise Distinct Summand
# 
# Represent a given positive integer number n as a sum of as many pairwise distinct positive integer
# as possible.
#
# n = a1 + a2 + ... + ak; ai > 0; ai != aj for all 1 <= i <= k
#
# Input:    integer n, 1 <= n <= 10^9
# Output:   First line: k number of integers that represents n as sum of k pairwise distinct 
#                       positive integers.
#           Second line: all k integers separated by space.

import random

# Read the input
n = int(input())

def pairwiseDistanctSum(n):

    pairs = []

    if n < 3:
        pairs.append(n)
    else:

        lowerBound = 1
        upperBound = n - lowerBound
        pairs.append(lowerBound)
        i = 0

        while True:

            if lowerBound == n:
                break

            lowerBound += pairs[i] + 1
            upperBound = n - lowerBound

            if pairs[i] + 2 > upperBound:

                lowerBound -= pairs[i] + 1
                pairs.append(n - lowerBound)
                break

            else:

                pairs.append(pairs[i] + 1)
                i += 1

    return pairs

# Method to stress testing the solution and ensure that everything works as expected
def stressTest(size):

    while False:

        result1 = pairwiseDistanctSum(0)
        result2 = pairwiseDistanctSum(0)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

# Using the fast solution
result = pairwiseDistanctSum(n)

print(len(result))
print(*result)

# Stress testing the solution
#stressTest(n)