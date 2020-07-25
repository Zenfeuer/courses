#!/bin/python3

# @author: Darwing Hernandez <darwinghga@gmail.com>

# Maximum Pairwise Product
# 
# Given a sequence of non-negative integers a_{0}, ... ,a_{n−1}, find the maximum pairwise product, 
# that is, the largest integer that can be obtained by multiplying two different elements from the
# sequence.
#
# Input:
# 
# The first line of the input contains an integer n. The next line contains n non-negative integers 
# a_{0}, ..., a_{n−1}​ (separated by spaces).
#
# Constraints:
#
# 2 <= n <= 10^5
# 0 <= a_{0}, ..., a_{n−1} <= 10^5

# Read the input
n = int(input())
a = [int(x) for x in input().split()]

# list: array of numbers (unsorted)
# isAsc: desired order. True: ascending | False: descending
def bubbleSort(list, isAsc):

    # saves the length of the list.
    n = len(list)

    # for each iteration, greatest/smallest element must be moved to n-i position in the array, this
    # ensures that the array it is ordered by the specified order (ascending or descending).
    for i in range(1, n):

        # j-th and (j+1)-th element must be compared to evaluate if they need to be swapped 
        # according to the desired order.
        for j in range(0, n - i):

            # isAsc and list[j] > list[j+1]:
            # if the desired order is ascending and the j-th element is greater than the (j+1)-th 
            # element, then a swap must be made.
            #
            # not isAsc and list[j] < list[j+1]:
            # if the desired order is descending and the j-th element is lesser than the (j+1)-th
            # element, then a swap must be made.
            if (isAsc and list[j] > list[j+1]) or (not isAsc and list[j] < list[j+1]):

                # Swapping j-th and (j+1)-th elements
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    # returns the sorted list
    return list

assert(len(a) == n)

# order the array of elements so to get the result is enough to multiply a[0] and a[1].
bubbleSort(a, False)

# printing the result
print(a[0] * a[1])