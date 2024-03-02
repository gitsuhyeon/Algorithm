def solution(d, budget):
    answer = 0
    if sum(d) <= budget:
        answer = len(d)
    else:
        while sum(d) > budget:
            d.sort(reverse = True)
            del d[0]
        answer = len(d)
    return answer