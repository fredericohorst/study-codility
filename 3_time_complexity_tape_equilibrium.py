
# TIME COMPLEXITY - TAPE EQUILIBRIUM PROBLEM @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):
    n = len(A)
    i = 1
    diff = []
    # values = []
    while i <= n:
        left = sum(A[:i])
        right = sum(A[i:n])
        # values.append(i)
        diff.append(abs(left-right))
        if i > n:
            break
        i += 1
    # return values[diff.index(min(diff))]
    return min(diff)


A = [3,1,2,4,3]

print(solution(A))
