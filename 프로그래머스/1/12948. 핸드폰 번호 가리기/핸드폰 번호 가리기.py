def solution(phone_number):
    answer = ''
    n = len(phone_number) - 4
    if n > 0:
        answer = '*' * n
    answer += phone_number[n:]
    return answer