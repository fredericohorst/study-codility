
# STACKS AND QUEUES - BRACKETS @ codility lessons
# by Frederico Horst
# source: https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/


def solution(S):
    valid = True
    stack = []
    for c in S:
        if c == "[" or c == "(" or c == "{":
            stack.append(c)
        elif c == ")":
            valid = False if not stack or stack.pop() != "(" else valid
        elif c == "]":
            valid = False if not stack or stack.pop() != "[" else valid
        elif c == "}":
            valid = False if not stack or stack.pop() != "{" else valid
    return 1 if valid and not stack else 0



# print(solution("{[()()]}"))

# print(solution("([)"))


print(solution("([)()]"))

