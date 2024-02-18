import math

def solution(n):
    answer = 0
    s = math.sqrt(n)
    if s - int(s) == 0:
        answer = int(pow(s+1,2))
    else:
        answer = -1
    return answer