def solution(n):
    list = [0] * 100001
    list[0] = 0
    list[1] = 1
    for i in range(2, n+1):
        list[i] = list[i-2] + list[i-1]
           
    return list[n] % 1234567
