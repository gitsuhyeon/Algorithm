def solution(citations):
    answer = 0
    bool = False
    idx = 0
    nc = sorted(citations)
    for i in range(len(nc)):
        if nc[i] <= len(nc)-i:
            if nc[i] >= i:
                answer = nc[i]
                bool = True

        elif nc[i] > len(nc)-i:
            if bool:
                idx = i
                break
    for j in range(nc[idx]-1, answer, -1):
        if j <= len(nc)-idx:
            answer = j
            break
        
    return answer