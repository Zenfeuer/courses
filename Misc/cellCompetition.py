#!/bin/python3

#d1

def cellCompetition(states, days):

    n = len(states)

    for i in range(days):
        for j in range(n):

            neighborL = 0
            neighborR = 0

            if j > 0:
                neighborL = prevState

            if j < n - 1:
                neighborR = states[j + 1]

            prevState = states[j]

            if neighborL == neighborR:
                states[j] = 0
            else:
                states[j] = 1

    return states

# Read the input
days = int(input())
states = [int(x) for x in input().split()]

print(cellCompetition(states, days))