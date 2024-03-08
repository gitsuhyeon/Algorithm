def solution(s):
    answer = ''
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            count = 0
            continue
            
        if count == 0:
            if s[i].isalpha():
                answer += s[i].upper()
            else:
                answer += s[i]
        else:
            if s[i].isalpha():
                answer += s[i].lower()
            else:
                answer += s[i]
        count += 1


            
    return answer