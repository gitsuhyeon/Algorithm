def solution(cards):
    answer = 0
    TF_table = [True] * len(cards)
    box = [0] * len(cards)
    trash = []
    i = 1
    j = 0
    while sum(box) < len(cards):
        if TF_table[i-1]:
            trash.append(i-1)
            box[j] += 1
            TF_table[i-1] = False
            i = cards[i-1]
        else:
            j += 1
            i += 1
            
    box.sort(reverse=True)
    answer = box[0] * box[1]
    return answer
