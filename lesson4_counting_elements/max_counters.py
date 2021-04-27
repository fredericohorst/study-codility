
# COUNTING ELEMENTS - MAX COUNTERS PROBLEM @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

def solution(X, A):
    river_positions = [False] * (X + 1)
    for time in range(len(A)):
        pos = A[time]
        if not river_positions[pos]:
            river_positions[time] = True
            X -= 1
            if X == 0: return time
    return -1
    # for r in range(X):
    #     # print('r pos:', r+1)
    #     res = [t for t in range(len(A)) if A[t] == r+1]
    #     if len(res) != 0:
    #         river[r] = A[min(res)]
    #     elif len(res) == 0:
    #         break 
    #     # return -1
    # return max(river)


# print(solution(5,[3,4,4,6,1,4,4])) # should be -1
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4])) # should be 6
# print(solution(3,[3,4,4,6,1,4,4])) # should be 
# print(solution(10,[1,3,1,4,2,3,5,4])) # should be 
