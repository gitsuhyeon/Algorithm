def solution(people, limit):
    answer = 0
    people.sort()
    idx = 0
    ridx = len(people)-1
    while idx <=ridx:
        answer += 1
        if people[idx]+people[ridx] <= limit:
            idx += 1
        ridx -= 1
    return answer