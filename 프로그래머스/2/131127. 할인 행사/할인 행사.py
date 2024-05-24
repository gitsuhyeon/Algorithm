def solution(want, number, discount):
    answer = 0
    temp = []
    for x,n in zip(want,number):
        temp.extend([x]*n)
    temp = sorted(temp)
    for i in range(len(discount)-9):
        subdiscount = discount[i:i+10]
        if temp == sorted(subdiscount):
            answer += 1
    return answer