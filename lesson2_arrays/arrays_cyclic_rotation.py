
# ARRAYS - CYCLIC ROTATION PROBLEM @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A,K):
    A_rotated = [None] * len(A)
    for i in range(len(A)):
        A_rotated[(i+K)%len(A)] = (A[i])

    return A_rotated


A = [3, 8, 9, 7, 6, 1]
K = 3
print(solution(A,K))
A = [7,2,8,3,5]
K = 1
print(solution(A,K))
print(solution([1, 2, 3, 4, 5], 2))
print(solution([1, 2, 3, 4, 5], 9))
print(solution([0 ,0 ,0], 1))
print(solution([3, 8, 9, 7, 6], 3)) # should be [9, 7, 6, 3, 8]
print(solution([-4], 0)) # should be [-4]
print(solution([-1, -2, 3, 4, 5], 2))
# print(type(A_rotated))
# got [-1, -2, -3, -4, -5, -.. expected [-3, -4, -5, -6, -1, -..

print(solution([3, 5, 1, 1, 2], 6))  # K > N
print(solution([3, 5, 1, 1, 2], 5))  # K = N 

print(solution([1, 1, 2, 3, 5], 42), 'expected: [3, 5, 1, 1, 2]', ) 