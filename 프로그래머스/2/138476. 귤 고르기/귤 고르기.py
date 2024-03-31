def solution(k, tangerine):
    answer = 0
    numlist = {}
    for num in tangerine:
        if num in numlist:
            numlist[num] += 1
        else:
            numlist[num] = 1
    numlist = sorted(numlist.items(), key = lambda x:x[1], reverse=True)
    i = 0
    while k > 0:
        k -= numlist[i][1]
        answer +=1
        i+= 1
        
    return answer