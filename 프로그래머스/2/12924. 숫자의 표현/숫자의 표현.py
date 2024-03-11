import math

def solution(n):
    answer = 1
    num = math.sqrt(2*n+0.25) - 0.5
    i = 2
    while i <= num:
        norm = i *(i+1)/2 
        if (n - norm) % i == 0:
            answer += 1
        i += 1
    return answer

"""4 15 r 3
14 4 2
5 : 15 20 25
4 : 10 14 18
3 : 6 9 12 15
2 : 3 5 7 9 12 15
"""