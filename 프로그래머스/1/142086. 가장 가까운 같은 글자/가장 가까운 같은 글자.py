def solution(s):
    answer = []
    temp = {}
    for i in range(len(s)):
        if s[i] in temp:
            answer.append(i - temp[s[i]])
        else:
            answer.append(-1)
        temp[s[i]] = i
    return answer