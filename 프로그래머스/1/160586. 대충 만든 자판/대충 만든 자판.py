def solution(keymap, targets):
    answer = [0] * len(targets)
    dictt = {}
    for i in range(len(targets)):
        state = True
        for j in range(len(targets[i])):
            if not targets[i][j] in dictt.keys():
                temp = []
                for k in range(len(keymap)):
                    temp.append
                    index = keymap[k].find(targets[i][j])
                    if index == -1:
                        continue
                    temp.append(index+1)
                if not temp:
                    state = False
                    break
                dictt[targets[i][j]] = min(temp)
            answer[i] += dictt[targets[i][j]]
        if not state:
            answer[i] = -1
            
            


    return answer