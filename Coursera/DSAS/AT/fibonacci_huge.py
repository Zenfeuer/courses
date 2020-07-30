#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Huge Fibonacci Number mod m
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

    if n <= 1:
        return n

    fn   = 0
    fi_0 = 0
    fi_1 = 1

    limit = n % pisanoIndex(m)

    i = 2

    if limit == 0: 
        return 0
    elif limit == 1: 
        return 1

    while i <= limit:

        fn   = (fi_0 + fi_1) % m
        fi_0 = fi_1
        fi_1 = fn

        i += 1

    return fn

params = [int(x) for x in input().split()]

print(fibonacciModM(params[0], params[1]))
