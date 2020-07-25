#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Maximum Pairwise Product
# 
# Given a sequence of non-negative integers a_{0}, ... ,a_{n−1}, find the maximum pairwise product, 
# that is, the largest integer that can be obtained by multiplying two different elements from the
# sequence.
#
# Input:
# 
# The first line of the input contains an integer n. The next line contains n non-negative integers 
# a_{0}, ..., a_{n−1}​ (separated by spaces).
#
# Constraints:
#
# 2 <= n <= 10^5
# 0 <= a_{0}, ..., a_{n−1} <= 10^5

import random

# Read the input
n = int(input())
a = [int(x) for x in input().split()]

# This solution is slow because it iterates and tests all posible pairs of integers, so it is O(n^2)
def maxPairwiseProductNaive(a, n):

    result = 0

    # this double iterations cause O(n^2)
    for i in range(0, n):
        for j in range(i+1, n):

            # this solution tests with each possible pair in the array
            if a[i]*a[j] > result:
                result = a[i]*a[j]

    return result

# This solution is better than the naive one because it finds the two greater integers in the array
# in just one iteration of the dataset, so we can say that is O(n)
def maxPairwiseProductFast(a, n):

    maxOne = -1
    maxTwo = -1
    i = 0

    while i < n:

        if maxOne < a[i]:
            
            if maxOne > maxTwo:
                maxTwo = maxOne

            maxOne = a[i]

        # if a possible greater integer is found but ignored by the first case because it is still
        # lesser than the already one stored in maxOne variable, it is needed to check if this
        # number it is greater than the one already stored at maxTwo
        elif maxTwo < a[i]:

            maxTwo = a[i]
        
        if (i+1) < n and maxTwo < a[i+1]:

            if maxTwo > maxOne:
                maxOne = maxTwo

            maxTwo = a[i+1]

        # Same here
        elif (i+1) < n and maxOne < a[i+1]:

            maxOne = a[i+1]

        i += 2
    
    return maxOne * maxTwo

# Method to stress testing the solution and ensure that everything works as expected
def stressTest(size):

    while True:

        randomSize = random.randint(2, size)
        testCase = random.sample(range(0, 100000), randomSize)

        print(randomSize)
        print(testCase)

        result1 = maxPairwiseProductNaive(testCase, randomSize)
        result2 = maxPairwiseProductFast(testCase, randomSize)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

# Using the fast solution
result = maxPairwiseProductFast(a, n)

# printing the result
print(result)

# Stress testing the solution
#stressTest(n)