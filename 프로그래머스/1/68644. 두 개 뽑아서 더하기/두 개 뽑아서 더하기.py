def solution(numbers):
    answer = []
    """if 0 in numbers:
        numbers.remove(0)
        answer = numbers"""
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            nnum = numbers[i] + numbers[j]
            if not nnum in answer:
                answer.append(nnum)
    answer.sort()
    
    return answer