
def solution(A):
    # write your code in Python 3.6
    act_sum = 0
    for number in A:
        act_sum += number # same of using sum(A)
    max_number = len(A) + 1
    expected_number = (max_number * (max_number + 1) // 2) # // python integer division
    return expected_number - act_sum


print('example: ', solution([2, 3, 1, 5])) # should return 4
print('continuous: ', solution([1, 2, 3, 4, 5, 6, 7, 8, 9])) # should return 10
print('empty: ', solution([])) # should return 1
print('two elements: ', solution([2,3])) # should return 1
print('two elements: ', solution([1,3])) # should return 2 
