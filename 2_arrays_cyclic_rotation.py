
# ARRAYS - CYCLIC ROTATION PROBLEM @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A,K):
    A_rotated = []
    A_rotated = A[K:len(A)]
    for i in range(K):
        A_rotated.append(A[i])
    return A_rotated


A = [3, 8, 9, 7, 6]
K = 3

print(solution(A,K))