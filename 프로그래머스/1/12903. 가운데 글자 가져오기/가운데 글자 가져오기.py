def solution(s):
    answer = ''
    l = len(s)
    num = l//2
    if l % 2 ==0:
        answer = s[num -1] 
    answer += s[num]
    return answer