

def solution(N,A):
    result = [0] * (N + 1)
    for i in range(len(A)):
        pos = A[i] # determinando a posição
        if pos < N: 
            result[pos] += 1
        else: # max counter case
            max_counter = max(result)
            result = [max_counter] * (N + 1)

    return result[1:]

print(solution(5, [3,4,4,6,1,4,4]), 'expected: [3,2,2,4,2]')
