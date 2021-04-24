
# TIME COMPLEXITY - TAPE EQUILIBRIUM PROBLEM @ codility lessons
# by Frederico Horst
# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/


def Solution(x,y,d):
    if x == y:
        jumps = 0
    elif x/d < .5:
        jumps = round(y/d)
    else:
        xd = x//d
        yd = y//d
        jumps = yd-xd

    return jumps



print(Solution(10, 85, 30)) # should be 3
print(Solution(10, 725, 40))
print(Solution(230, 1435, 34))
print(Solution(10, 10, 0))
print(Solution(2, 11, 3)) # should be 3
print(Solution(5, 105, 3)) # should be 34
print(Solution(213,1000000000,2)) 
print(Solution(1,1000000000,1283))