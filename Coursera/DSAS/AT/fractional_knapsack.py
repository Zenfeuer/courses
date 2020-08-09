#!/bin/python3
# @author: Darwing Hernandez <darwinghga@gmail.com>

# Fractional Knapsack
#
# Input:    integer n; 1 <= n <= 10^3
#           integer W; 0 <= W <= 2*10^6
#           integers vi; 0 <= vi <= 2*10^6; 1 <= i <= n
#           integers wi; 0 <= wi <= 2*10^6; 1 <= i <= n
# Output:   Output the maximal value of fractions of items that fit into the knapsack.

import random

def fractionalKnapsack(n, W, elements):

    V = 0.0000

    for elem in elements:

        if W == 0:
            return V

        a = min(elem[1], W)
        V += a*(elem[0]/elem[1])
        W -= a
    
    return V


# Stress testing both solutions
#TODO

params = [int(x) for x in input().split()]

n = params[0]
W = params[1]
i = 0
elements = []

for i in range(n):
    element = [int(x) for x in input().split()]
    element.append(element[0]/element[1])
    elements.append(element)

# Stress testing
#stressTest(n)

elements = sorted(elements, key=lambda element: element[2], reverse = True)

# Call fast solution
print("%.4f" % fractionalKnapsack(n, W, elements))