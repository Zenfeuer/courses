#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Sum of Fibonacci Numbers
#

def pisanoIndex(m):

    pisano = 0

    fn   = 0 # fib(n)%m
    fi_0 = 0 # Base case fib(0)
    fi_1 = 1 # Base case fib(1)

    while True:

        if pisano > 0 and fi_0%m == 0 and fi_1%m == 1:
            break

        fn   = (fi_0 + fi_1) % m
        fi_0 = fi_1
        fi_1 = fn

        pisano += 1

    return pisano

def fibonacciModM(n, m):

    fn   = 1
    fi_0 = 0
    fi_1 = 1

    limit = n % pisanoIndex(m)

    for i in range(2, limit + 1):
        
        fn   = (fi_0 + fi_1) % m
        fi_0 = fi_1
        fi_1 = fn

    return fn

n = int(input())

def sumFibNumbers(n):

    result = fibonacciModM(n + 2, 10)

    if result == 0:
        result = 9
    else:
        result -= 1

    return result

print(sumFibNumbers(n))


