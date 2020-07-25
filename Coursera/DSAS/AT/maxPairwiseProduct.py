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

# Read the input
n = int(input())
a = [int(x) for x in input().split()]

maxOne = -1
maxTwo = -1
i = 0

while i < n:

    if maxOne < a[i]:
        
        if maxOne > maxTwo:
            maxTwo = maxOne

        maxOne = a[i]

    elif maxTwo < a[i]:

        if maxTwo > maxOne:
            maxOne = maxTwo

        maxTwo = a[i]
    
    if (i+1) < n and maxTwo < a[i+1]:

        if maxTwo > maxOne:
            maxOne = maxTwo

        maxTwo = a[i+1]
        
    i += 2

# printing the result
print(maxOne * maxTwo)