def solution(k, ranges):
    answer = []
    s = []
    count = 0
    while k != 1:
        temp = k
        if k %2 == 0:
            k /= 2
            s.append((k+temp)/2.0)
        else:
            k = k*3 +1 
            s.append((k+temp)/2.0)
        count += 1
        
    for r in ranges:
        r[1] += count  
        if r[0] == r[1]:
            answer.append(0.0)
        elif r[0] > r[1]:
            answer.append(-1.0)
        else:
            answer.append(sum(s[r[0]:r[1]]))
        
    return answer