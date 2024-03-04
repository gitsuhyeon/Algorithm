def solution(s, n):
    answer = ''
    s = list(s)
    for alp in s:
        if alp == ' ':
            answer += ' '
        else:
            if ord(alp) + n > 122 :
                answer += chr(ord(alp)+n-26)
            elif ord(alp) <= 90 and ord(alp) +n > 90:
                answer += chr(ord(alp)+n-26)
            else:
                answer += chr(ord(alp) + n)
    return answer