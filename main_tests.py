
import random

import lesson3_time_complexity.perm_missing_element as pme

# easy
A = [2,3,1,5]
print(A)
print(pme.solution(A))
print('################################')
# empty list
A = []
print(A)
print(pme.solution(A))
print('################################')
# single list
A = [1]
print(A)
print(pme.solution(A))
print('################################')
# missing first or last
A = [2,3,4,6]
print(A)
print(pme.solution(A))
print('################################')
A = [2,3,7]
print(A)
print(pme.solution(A))
print('################################')
# medium
A = [random.randint(1,10000) for i in range(0,10000)]
print(A)
print(pme.solution(A))
print('################################')
# large
A = [random.randint(1,100000) for i in range(0,100000)]
print(A)
print(pme.solution(A))
print('################################')



    