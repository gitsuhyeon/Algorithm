def solution(n):
    answer = 0
    size = len(str(n))
    for i in range(size):
        answer += n % 10
        n = n // 10

    return answer