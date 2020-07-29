#!/bin/python3
#d2

def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a%b)

def gcdNumbers(num, arr):

    for i in range(num - 1):
        arr[i+1] = gcd(arr[i], arr[i+1])

    return arr[num-1]

num = int(input())
arr = [int(x) for x in input().split()]

print(gcdNumbers(num, arr))