def solution(k, score):
    answer = []
    temp = []
    for i in range(len(score)):
        if i < k:
            temp.append(score[i])
            answer.append(min(temp))
        else:
            temp.append(score[i])
            temp.sort(reverse = True)
            answer.append(temp[k-1])
        
            
        
    return answer