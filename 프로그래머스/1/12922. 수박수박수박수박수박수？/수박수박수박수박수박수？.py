def solution(n):
    answer = ''
    string = "수박"
    n = int(n)
    num = n//2
    if n % 2 == 0:
        answer = string * num
    else:
        answer = string * num + "수"
    return answer