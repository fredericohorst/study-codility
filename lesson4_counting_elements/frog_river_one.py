
# COUNTING ELEMENTS - FROG RIVER ONE PROBLEM @ codility lessons
# by Frederico Horst

def solution(X, A):
    river_positions = [False] * (X + 1)
    for time in range(len(A)):
        pos = A[time]
        if not river_positions[pos]:
            river_positions[pos] = True
            X -= 1
            if X == 0: return time
    return -1



print(solution(5,[3,4,4,6,1,4,4])) # should be -1
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4])) # should be 6
print(solution(3,[3,4,4,6,1,4,4])) # should be 
print(solution(10,[1,3,1,4,2,3,5,4])) # should be 
