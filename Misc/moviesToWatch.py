#!/bin/python3

def moviesToWatch(flightDuration, numMovies, movieDuration):
    
    realFlightDuration = flightDuration - 30

    if numMovies == 2:
        return 0, 1
    else:

        sortedMovies = sorted(movieDuration)
        indexes = { v: i for i,v in enumerate(movieDuration) }

        movieIndex1 = -1
        movieIndex2 = -1
        i = numMovies - 1

        while i > 0:

            if sortedMovies[i] < realFlightDuration:

                j = i - 1

                while j >= 0:

                    pairMoviesDuration = sortedMovies[i] + sortedMovies[j]

                    if pairMoviesDuration == realFlightDuration:

                        movieIndex1 = indexes[sortedMovies[i]]
                        movieIndex2 = indexes[sortedMovies[j]]
                        break

                    j -= 1

            if movieIndex1 != -1 and movieIndex2 != -1:
                break

            i -= 1
    
    return movieIndex1, movieIndex2

flightDuration = int(input())
numMovies = int(input())
movieDuration = [int(x) for x in input().split()]

print(moviesToWatch(flightDuration, numMovies, movieDuration))