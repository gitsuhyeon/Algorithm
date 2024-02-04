def solution(n, m, section):
    answer = 0
    ran = 0
    for num in section:
        if num >= ran:
            ran = num+m
            answer += 1
    return answer