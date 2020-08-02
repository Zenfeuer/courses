#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Fibonacci
# 
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)

import random

# Recursive version that is slow because it calculates some same cases several times
def fibonacciNaive(n):

    if n <= 1:
        return n
    else:
        return fibonacciNaive(n-1) + fibonacciNaive(n-2)

# Iterative version that is faster because each case is calculated once
def fibonacciFast(n):

    if n <= 1:
        return n

    f0 = 0
    f1 = 1
    fn = 0
    i = 2

    while i <= n:

        fn = f0 + f1
        f0 = f1
        f1 = fn

        i += 1

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

n = int(input())

# Stress testing
#stressTest(n)

# Call fast solution
print(fibonacciFast(n))