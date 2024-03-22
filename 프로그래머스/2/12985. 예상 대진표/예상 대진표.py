def solution(n,a,b):
    answer = 0
    if a == b:
        return 0
    return solution(n/2,(a+1)//2,(b+1)//2)+1

    return answer