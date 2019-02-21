# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

def minCost (matrix):
    #given a n and k, find the lowest k that is not the last k, return result
    #the matrix's first column is houses and the rest are colours
    #list P = [(n+k), (n1+k1), ...]
    #we have to use the lowest k while the current (n+k) != the last (n+k)
    #add up the list and there is the price
    #assume all k prices are different

    allK = matrix[0]
    allK.remove(0)
    allK.sort()

    for i in matrix:
        