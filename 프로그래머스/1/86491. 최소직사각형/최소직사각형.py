def solution(sizes):
    answer = 0
    norm = max(sizes)
    for num in sizes:
        if num[0] < num[1]:
            num[1] , num[0] = num[0], num[1]
        if num[0] > norm[0]:
            norm[0] = num[0]
        if num[1] > norm[1]:
            norm[1] = num[1]
    answer = norm[0] * norm[1]
    return answer