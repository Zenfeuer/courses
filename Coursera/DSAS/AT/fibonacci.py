#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Fibonacci
# 
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)

import random

n = int(input())

# Recursive version that is slow
def fibonacciNaive(n):

    if n <= 1:
        return n
    else:
        return fibonacciNaive(n-1) + fibonacciNaive(n-2)

# Iterative version that is faster
def fibonacciFast(n):

    if n <= 1:
        return n

    f0 = 0
    f1 = 1
    fn = 0

    for i in range(2, n+1):

        fn = f0 + f1
        f0 = f1
        f1 = fn

    return fn

# Stress testing both solutions
def stressTest(n):

    while True:

        randomSize = random.randint(0, n)

        print(randomSize)

        result1 = fibonacciNaive(randomSize)
        result2 = fibonacciFast(randomSize)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

# Stress testing
#stressTest(n)

# Call fast solution
result = fibonacciFast(n)

# Print result
print(result)