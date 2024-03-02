def solution(s):
    answer = ''
    idx = -1
    for i in range(len(s)):
        idx += 1
        if s[i] == ' ':
            idx = -1
            answer += s[i]
        elif idx % 2 == 0:
            answer += s[i].upper()
        elif idx % 2 == 1:
            answer += s[i].lower()
    return answer