def solution(bandage, health, attacks):
    answer = 0
    hp = health
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    current_time = 0
    combo = 0
    last_attackt = attacks[-1][0]
    i = 0
    while current_time <= last_attackt:
        if current_time == attacks[i][0]:
            hp -= attacks[i][1]
            if hp <= 0:
                break
            combo = 0
            i += 1
        elif hp < health:
            hp += x
            if hp > health:
                hp = health
            combo += 1
            if combo >= t:
                hp += y
                if hp > health:
                    hp = health
                combo = 0
        current_time += 1

    
    if hp <= 0:
        answer = -1
    else:
        answer = hp

    
    return answer