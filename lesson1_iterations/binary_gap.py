
# BINARY GAP PROBLEM @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/


def solution(N):
    x = N
    dist_local = 0
    dist_max = 0
    bef_rest = 0
    while x >= 1:
        # print('x', x)
        r = x % 2
        # print('r', r)
        x = x // 2
        if r != 0:
            bef_rest = r
            if dist_local > dist_max: dist_max = dist_local
            dist_local = 0
        elif r == 0 and bef_rest != 0:
            dist_local = 1
            bef_rest = r
            if dist_local > dist_max: dist_max = dist_local
        elif r == 0 and bef_rest == 0 and dist_local != 0: # apenas considerar se já tiver dist_local
            dist_local += 1
            if dist_local > dist_max: dist_max = dist_local
        # print('bef_rest', bef_rest)
        # print('dist_local', dist_local)
        # print('dist_max', dist_max)
    # if first_rest1 == 0: dist_max = 0 # ?
    return x,r,dist_local, dist_max
    # return dist_max



# print('529',solution(529))
# print('9',solution(9))
# print('32',solution(32))
# print('246',solution(246))
print('1041',solution(1041))