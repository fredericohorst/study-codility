def solution(A):
    # write your code in Python 3.6

    if len(A)>0: A.sort()
    else: b=1

    for n in range(0,len(A)):
        if n + 1 < A[n]:
            b = n+1
            print(n)
        elif n + 1 == A[n]:
            b = 1

    return b


print('example: ', solution([2, 3, 1, 5]))
print('continuous: ', solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print('empty: ', solution([]))
print('single: ', solution([3]))
print('double: ', solution([2,3]))
print('double: ', solution([1,3]))
