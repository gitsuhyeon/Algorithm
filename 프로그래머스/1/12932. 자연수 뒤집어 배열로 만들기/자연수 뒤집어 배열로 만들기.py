def solution(n):
    answer = []
    nl = str(n)
    for i in range(len(nl)-1,-1,-1):
        answer.append(int(nl[i]))
    return answer