
# COUNTING ELEMENTS - MAX COUNTERS PROBLEM @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

def solution(N,A):
    counters = [0] * N
    start_line = 0
    current_max = 0
    for i in A:
        x = i - 1
        if i > N:
            start_line = current_max
        elif counters[x] < start_line:
            counters[x] = start_line + 1
        else:
            counters[x] += 1
        if i <= N and counters[x] > current_max:
            current_max = counters[x]
        for i in range(0, len(counters)):
            if counters[i] < start_line:
                counters[i] = start_line
    return counters






N = 5
A = [3,4,4,6,1,4,4]
# index = x - 1

print(A[0])
print(A[1])

print(solution(N,A))

