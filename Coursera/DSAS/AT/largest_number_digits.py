#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Maximazing Number using Digits
# 
# Input:    

import random

# Read the input
n = int(input())
digits = [int(x) for x in input().split()]

digits = sorted(digits, reverse = True)

def largestNumber(digits):

    bigNumber = ""

    for digit in digits:

        if bigNumber == "":

            bigNumber = str(digit)

        else:

            strDigit = str(digit)

            if strDigit[0] >= bigNumber[0]:

                bigNumber = strDigit + bigNumber
            
            else:

                bigNumber += strDigit

    return bigNumber

# Method to stress testing the solution and ensure that everything works as expected
def stressTest(size):

    while False:

        result1 = largestNumber(0)
        result2 = largestNumber(0)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

# Using the fast solution
result = largestNumber(digits)
print(result)

# Stress testing the solution
#stressTest(n)