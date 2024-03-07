def solution(food):
    answer = ''
    num1 = ''
    for i in range(1,len(food)):
        if food[i] > 1:
            p = food[i] // 2
            num1 += str(i) * p
    answer = num1 + '0' + num1[::-1]
            
            
                
    return answer