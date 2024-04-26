def solution(ingredient):
    answer = 0
    temp = []
    for igd in ingredient:
        temp.append(igd)
        if igd == 1 and len(temp) >= 4:
            if temp[-2] ==3 and temp[-3] == 2 and temp[-4] == 1:
                del temp[-4:]
                answer += 1


    return answer