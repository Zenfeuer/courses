#!/bin/python3
# @author: Darwing Hernandez <darwinghga@gmail.com>

# Min of Refills for a Car that travels from A to B
#
# Greedy algorithm to resolve the minimum refills that a car needs to do for travel from a point A
# to point B where there are several gas stations between those points

# x: all the points in ascending order, including A and B
# n: length of x
# L: maximum kilometers that the car can travel without refilling
def minRefills(x, n, L):

    numRefills = 0
    currentRefill = 0

    while currentRefill < n - 1:

        lastRefill = currentRefill

        while currentRefill < n - 1 and x[currentRefill + 1] - x[lastRefill] <= L:
            currentRefill += 1

        if currentRefill == lastRefill:
            return -1
        
        if currentRefill < n - 1:
            numRefills += 1

    return numRefills

L = int(input())
x = [int(x) for x in input().split()]

print(minRefills(x, len(x), L))