def solution(friends, gifts):
    answer = 0
    n = len(friends)
    table = [[]] * n
    for i in range(n):
        table[i] = [0] * n
    for i in range(len(gifts)):
        ngift = gifts[i].split()
        a = friends.index(ngift[0])
        b = friends.index(ngift[1])
        table[a][b] +=1
    gift_rate = [0] * n
    for i in range(n):
        gift_rate[i] = sum(table[i])
        for j in range(len(friends)):
            rec = table[j][i]
            gift_rate[i] -= rec
    giventake = [0] * n
    for i in range(n):
        for j in range(i+1,n):
            if table[i][j] > table[j][i]:
                giventake[i] += 1
            elif table[i][j] == table[j][i]:
                if gift_rate[i] > gift_rate[j]:
                    giventake[i] +=1
                elif gift_rate[i] == gift_rate[j]:
                    giventake[i] += 0
                elif gift_rate[i] < gift_rate[j]:
                    giventake[j] += 1
                
            elif table[i][j] < table[j][i]:
                giventake[j] += 1
                
    answer = max(giventake)     
    return answer