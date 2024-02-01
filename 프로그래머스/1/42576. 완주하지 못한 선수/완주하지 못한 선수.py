def solution(participant, completion):
    answer = ''
    dictc ={}
    for i in range(len(participant)):
        if participant[i] in dictc.keys():
            dictc[participant[i]] += 1
        else:
            dictc[participant[i]] = 1
    for i in range(len(completion)):
        dictc[completion[i]] -= 1
    
    for k,v in dictc.items():
        if v != 0:
            answer = k
            
    return answer