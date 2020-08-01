#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Huge Fibonacci Number mod m
#
# Compute F(n) mod m, where n may be really huge: up to 10^18. For such values of n, an algorithm
# looping for n iterations will not fit into one second for sure.
#
# Fib(n) mod m is periodic for any integer m >= 2. This period is known as Pisano period (https://oeis.org/A001175).
# Pisano period begins always with 01.
#
# Input:   integer n; 1 <= n <= 10^18
#          integer m; 2 <= m <= 10^5
# Output:  Fib(n) mod m

import random


# Iterative version that is faster because each case is calculated once. Now this is going to be our
# naive solution
def fibonacciModMNaive(n, m):

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

    return fn % m

# Determines the pisano index where the period begins again. This helps us to know the index for the
# period to calculate then the F(n) mod m
def pisanoIndex(m):

    pisano = 0

    fn   = 0 # fib(n)%m
    fi_0 = 0 # Base case fib(0)
    fi_1 = 1 # Base case fib(1)

    while True:

        # This means that we already found the period
        if pisano > 0 and fi_0%m == 0 and fi_1%m == 1:
            break

        fn   = (fi_0 + fi_1) % m
        fi_0 = fi_1
        fi_1 = fn

        pisano += 1

    return pisano

# Fast solution for F(n) mod m where the index for the period is previously calculated and after
# get the F(n) mod m
def fibonacciModM(n, m):

    # Base case
    if n <= 1:
        return n

    # Determines the limit of iterations to calculate F(n) mod m. This is because it is using the
    # approach that F(n) mod m is periodic for m >= 2, so F(n) mod m = F(n') mod m, for n' < n.
    limit = n % pisanoIndex(m)

    # Base case
    if limit <= 1:
        return limit

    fn   = 0
    fi_0 = 0
    fi_1 = 1

    i = 2

    # Calculates the mod m with the new and smaller "n".
    while i <= limit:

        fn   = (fi_0 + fi_1) % m
        fi_0 = fi_1
        fi_1 = fn

        i += 1

    return fn

# Stress testing both solutions
def stressTest(n, m):

    while True:

        newN = random.randint(1, n)
        newM = random.randint(2, m)

        print(newN, newM)

        result1 = fibonacciModMNaive(newN, newM)
        result2 = fibonacciModM(newN, newM)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

params = [int(x) for x in input().split()]

# Stress testing
#stressTest(params[0], params[1])

print(fibonacciModM(params[0], params[1]))
