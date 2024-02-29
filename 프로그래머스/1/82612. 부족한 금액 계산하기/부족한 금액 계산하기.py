def solution(price, money, count):
    answer = 0
    money -= price * count * (count+1) / 2
    if money >= 0:
        answer = 0
    else:
        answer -= money
    return answer