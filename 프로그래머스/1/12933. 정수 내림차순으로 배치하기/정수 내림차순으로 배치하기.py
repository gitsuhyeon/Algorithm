def solution(n):
    answer = 0
    a = list(str(n))
    a.sort(reverse = True)
    b = "".join(a)
    answer = int(b)
    return answer