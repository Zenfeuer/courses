#!/bin/python3
# @author: Darwing Hernandez <darwinghga@gmail.com>

# Covering Segments
#
# Given a set of n segments {[a_0, b_0], [a_1, b_1],..., [a_n-1, b_n1-]} with integer coordinates on
# a line, find the minimum number m of points such that each segment contains at least one point. 
# That is, find a set of integers X of the minimum size such that for any segment [a_i, b_i] there 
# is a point x belongs to X such that a_i <= x <= b_i.
#
# Input:    
# Output:   

import random

def coveringSegments(points):

    currentPoint = points[0]
    coveredPoints = [currentPoint[1]]

    for i in range(1, len(points)):

        if (points[i][0] > currentPoint[1]):

            currentPoint = points[i]
            coveredPoints.append(currentPoint[1])

    print(len(coveredPoints))
    print(*coveredPoints)

# Stress testing both solutions
#TODO

n = int(input())
points = []

while n > 0:
    point = [int(x) for x in input().split()]
    points.append(point)
    n -= 1

# Stress testing
#stressTest(n)

# Safe move it is sort the points by their maximum value
points = sorted(points, key=lambda point: point[1])

# Call fast solution
coveringSegments(points)