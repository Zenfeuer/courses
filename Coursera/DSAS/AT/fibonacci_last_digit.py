#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Last Digit of a Large Fibonacci Number
#
# To get the last digit for a large fibonacci number, the fast approach is to carry the last digit
# using mod 10
# 
# F(0) = 0
# F(1) = 1
# F(n) = (F(n-1) + F(n-2)) mod 10
#
# Input:   integer n; 0 <= n <= 10^7
# Output:  Fib(n) mod 10

import random

n = int(input())

# Recursive version that is slow
def lastDigitFibNaive(n):

    if n <= 1:
        return n
    else:
        return (lastDigitFibNaive(n-1) + lastDigitFibNaive(n-2)) % 10

# Iterative version that is faster
def lastDigitFibFast(n):

    if n <= 1:
        return n

    f0 = 0
    f1 = 1
    fn = 0
    i = 2

    while i <= n:

        fn = (f0 + f1) % 10
        f0 = f1
        f1 = fn

        i += 1

    return fn

# Stress testing both solutions
def stressTest(n):

    while True:

        randomSize = random.randint(0, n)

        print(randomSize)

        result1 = lastDigitFibNaive(randomSize)
        result2 = lastDigitFibFast(randomSize)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

# Stress testing
#stressTest(n)

print(lastDigitFibFast(n))