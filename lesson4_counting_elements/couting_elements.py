

def counting(A, m):
    n = len(A) 
    # count=[0]*(m+1) 
    count=[0]*(n+1) 
    for k in range(n):
        count[A[k]] += 1 
    return count

print(counting([1,2,3,4,5,6,7,8,9],3))
print(counting([1,2,3,4,5,6,7,8,9],9))


def slow_solution(A,B,m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(n): 
            change = B[j] - A[i] 
            sum_a += change 
            sum_b -= change
    if sum_a == sum_b: 
        return True 
    sum_a -= change 
    sum_b += change
    return False

