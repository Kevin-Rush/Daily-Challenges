# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], 
# which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# class Solution { public int solution(int[] A); }

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].
def solution(A):
    # write your code in Python 3.6
    
    if (len(A) <= 1):
        return len(A) + 1
    else:
        big = A[0]
        sum = 0

        for i in A:
            if i>big:
                big = i
            sum += i
        n = big 
        seqSum = (n*(n+1))/2

        if seqSum - sum == 0:
            return big+1
        else:
            return int(seqSum-sum)

print(solution([1,2,3,4,5,6,7,8]))