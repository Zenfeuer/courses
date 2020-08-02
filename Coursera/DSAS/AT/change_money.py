#!/bin/python3
# @author: Darwing Hernandez <darwinghga@gmail.com>

# Changing Money
# 
# Find the minimum number of coins needed to change the input value (an integer) into coins with
# denominations 1, 5, and 10
#
# Input:    integer m; 1 <= m <= 10^3
# Output:   minimum number of coins with denominations 1, 5, 10 that changes m.

import random

def changeMoney(m):

    numberCoins = 0

    numberCoins += m//10
    m = m%10
    numberCoins += m//5
    m = m%5
    numberCoins += m

    return numberCoins

# Stress testing both solutions
def stressTest(n):

    while True:

        randomSize = random.randint(0, n)

        print(randomSize)

        result1 = changeMoney(randomSize)
        result2 = changeMoney(randomSize)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

m = int(input())

# Stress testing
#stressTest(n)

# Call fast solution
print(changeMoney(m))