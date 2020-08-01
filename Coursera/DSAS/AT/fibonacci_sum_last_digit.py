#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Sum of Fibonacci Numbers
#
# Given an integer n, find the last digit of the sum F(0) + F(1) + ... + F(n).
#
# The idea is to find a representation for the serie S(n) = F(0) + F(1) + ... + F(n). To achieve 
# that, each Fibonacci number can be represented as follows:
#
# F(n+1) = F(n)   + F(n-1) => F(n-1) = F(n+1) - F(n)
# F(n)   = F(n-1) + F(n-2) => F(n-2) = F(n)   - F(n-1)
# F(n-1) = F(n-2) + F(n-3) => F(n-3) = F(n-1) - F(n-2)
#  ...          ...                     ...
# F(3)   = F(2)   + F(1)   => F(1)   = F(3)   - F(2)
# F(2)   = F(1)   + F(0)   => F(0)   = F(2)   - F(1)
#
# Now, F(n-1) + F(n-2) + ... + F(1) + F(0) = F(n+1) - F(1) = F(n+1) - 1 = S(n-1)
# Then, for n, the serie is S(n) = F(n+2) - 1
#
# Input:    integer n; 0 <= n <= 10^14
# Output:   last digit of F(0) + F(1) + ... + F(n).

import random


# Iterative version that is faster because each case is calculated once. Now this is going to be our
# naive solution.
def lastDigitSumFibNumberNaive(n):

    if n <= 1:
        return n

    f0 = 0
    f1 = 1
    fn = 0
    i = 2

    sn = 1

    while i <= n:

        fn = f0 + f1
        f0 = f1
        f1 = fn
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
# determined that the sum of n Fibonacci numbers can be reduced to S(n) = F(n+2) - 1, but n can be
# really huge, so the better aproach to do that is using F(n) mod m, where m = 10.
def lastDigitSumFibNumberFast(n):

    # Get the last digit
    result = fibonacciModM(n + 2, 10)

    # Because the serie is S(n) = F(n+2) - 1, it is needed to substract 1 to the result.
    result -= 1

    # Failover case if the last digit is zero (0).
    if result < 0:
        result = 9

    return result

# Stress testing both solutions
def stressTest(n):

    while True:

        randomN = random.randint(1, n)

        print(randomN)

        result1 = lastDigitSumFibNumberNaive(randomN)
        result2 = lastDigitSumFibNumberFast(randomN)

        if result1 != result2:
            print("Wrong answer: ", result1, result2)
            break
        else:
            print("OK")

n = int(input())

# Stress testing
#stressTest(n)

print(lastDigitSumFibNumberFast(n))