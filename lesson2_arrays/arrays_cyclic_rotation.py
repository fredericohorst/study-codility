
# ARRAYS - CYCLIC ROTATION PROBLEM @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A,K):
    A_rotated = [None] * len(A)

    for i in range(len(A)):
        A_rotated[(i + K) % len(A)] = A[i]

    return A_rotated


A = [3, 8, 9, 7, 6, 1]
K = 3

print(solution(A,K))
print(solution([1, 2, 3, 4, 5], 2))
print(solution([1, 2, 3, 4, 5], 9))
# print(type(A_rotated))
