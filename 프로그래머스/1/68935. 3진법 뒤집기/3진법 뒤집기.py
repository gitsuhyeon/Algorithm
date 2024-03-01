def solution(n):
    answer = 0
    temp = []
    i = 3
    while i <= n:
        i = i * 3
    if i > n:
        i = i / 3
    t = 0
    while n > 0:
        l = n // i
        answer += l * pow(3,t)
        print(answer)
        n = n % i
        i = i / 3 
        t += 1

    return answer