# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
from bisect import bisect_left
C = [-1, -2, 4, 5, 6, 12, 3, 4, 1, 0]
B = []
D = [-3, -4, -12312312, 2, 3, 1, 5, 5]

def solution(A):
    noNeg = list(filter(lambda x: x > 0, A))
    minVal = 1
    if len(noNeg) is 0:
        return minVal
    for N in sorted(noNeg):
        if N is minVal - 1:
            continue
        elif  N is not minVal:
            return minVal
        else:
            minVal += 1
    return minVal


solution(C)
solution(B)
solution(D)
