def solution(operations):
    answer = []
    for num in operations:
        if num[0] == "I":
            answer.append(int(num[2:]))
        if num[0] == "D":
            if num[2] == "1":
                if answer:
                    answer.remove(max(answer))
            if num[2] == "-":
                if answer:
                    answer.remove(min(answer))
    if not answer:
        return [0,0]
    answer = [max(answer),min(answer)]
    return answer