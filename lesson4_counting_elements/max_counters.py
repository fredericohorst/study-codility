

def solution(N,A):
    result = [0] * (N) # counters
    start_line = 0
    current_max = 0

    for i in A:
        index = i - 1 # índices começam no zero
        if i > N: # max counter case
            start_line = current_max
        elif result[index] < start_line:
            result[index] = start_line + 1
        else:
            result[index] += 1
        if i <= N and result[index] > current_max:
            current_max = result[index]

    for i in range(0, len(result)):
        if result[i] < start_line:
            result[i] = start_line

    return result

print(solution(5, [3,4,4,6,1,4,4]), 'expected: [3,2,2,4,2]')
# print(solution(1, [1]), 'expected: [1]')
