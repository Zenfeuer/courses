#!/bin/python3

def gcd(a, b):

    if b == 0:
        return a
    
    return gcd(b, a%b)


print(gcd(3, 99))
