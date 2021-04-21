
# TIME COMPLEXITY - TAPE EQUILIBRIUM PROBLEM @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):
    x = A[0]
    y = sum(A) - A[0]
    z = abs(x-y)
    for i in range(1,len(A)-1):
        x += A[i]
        y -= A[i]
        z_new = abs(x-y)
        if z_new < z:
            z = z_new

    # return min(z), z.index(min(z))+1
    return z

A = [3,1,2,4,3]
print(solution(A))

A = [3,4,1,8,2,10,7,8,4,3,1,9]
print(solution(A))
