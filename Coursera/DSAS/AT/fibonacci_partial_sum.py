#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Partial Sum of Fibonacci Numbers
#
# Given two non-negative integers m and n, where m ≤ n, find the last digit of the sum 
# F(m) + F(m+1) + ... + F(n-1) + F(n).
#
# The idea is to find a representation for the serie S(m,n) = F(m) + F(m+1) + ... + F(n-1) + F(n).
# To achieve that, each Fibonacci number can be represented as follows:
# 
# F(n+1) = F(n)   + F(n-1) => F(n-1) = F(n+1) - F(n)
# F(n)   = F(n-1) + F(n-2) => F(n-2) = F(n)   - F(n-1)
# F(n-1) = F(n-2) + F(n-3) => F(n-3) = F(n-1) - F(n-2)
#  ...          ...                     ...
# F(m+3) = F(m+2) + F(m+1) => F(m+1) = F(m+3) - F(m+2)
# F(m+2) = F(m+1) + F(m)   => F(m)   = F(m+2) - F(m+1)
#
# Now, F(n-1) + F(n-2) + ... + F(m+1) + F(m) = F(n+1) - F(m+1) = S(m,n-1)
# Then, for n, the serie is S(n) = F(n+2) - F(m+1)
#
# Input:    two integers n and m; 0 <= m <= n <= 10^18
# Output:   last digit of F(m) + F(m+1) + ... + F(n).

import random


# Iterative version. Now this is going to be our naive solution.
def partialSumFibNumbersNaive(m, n):

    if n <= 1:
        return n

    f0 = 0
    f1 = 1
    fn = 0
    i = 2

    sn = 0

    # Failover case
    if m <= 1:
        sn = 1

    while i <= n:

        fn = f0 + f1
        f0 = f1
        f1 = fn

        # begins to sum when i reaches m
        if i >= m:
            sn += fn

        i += 1

    return sn % 10

# Determines the pisano index where the period begins again. This is used for this solution also
# because n can be really huge (10^14), so it is better to use the F(n) mod m approach for m = 10
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

# Fast solution for F(n) mod 10 where the index for the period is previously calculated and after
# get the F(n) mod 10
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

# Fast solution to get the last digit for a huge Fibonacci number. To achieve that, it was 
# determined that the sum of partial Fibonacci numbers can be reduced to S(n, m) = F(n+2) - F(m+1),
# but both n and m can be really huge, so the better aproach to do that is using F(n) mod m. For
# this case, using m = 10 can get time limit because the numbers can be really very huge (10^18), so
# using a multiple of 10, for example 60, can help to reduce the number of cases
def partialSumFibNumbers(m, n):

    # Get the two Fibonacci numbers mod m (for this case, 60)
    fib1 = fibonacciModM(n + 2, 60)
    fib2 = fibonacciModM(m + 1, 60)

    # Get the last digit
    return (fib1 - fib2)%10

# Stress testing both solutions
def stressTest(m, n):

    while True:

        randomN = random.randint(m, n)
        randomM = random.randint(0, m)

        print(randomM, randomN)

        result1 = partialSumFibNumbersNaive(randomM, randomN)
        result2 = partialSumFibNumbers(randomM, randomN)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

params = [int(x) for x in input().split()]

#Stress testing
#stressTest(params[0], params[1])

print(partialSumFibNumbers(params[0], params[1]))


