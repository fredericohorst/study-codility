
# TIME COMPLEXITY - TAPE EQUILIBRIUM PROBLEM @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):
    n = len(A)
    z = [] # min value
    for i in range(1,n):
        x = sum(A[0:i])
        y = sum(A[i:n])
        z.append(abs(x-y))

    return min(z), z.index(min(z))+1

A = [3,1,2,4,3]
print(solution(A))

A = [3,4,1,8,2,10,7,8,4,3,1,9]
print(solution(A))
