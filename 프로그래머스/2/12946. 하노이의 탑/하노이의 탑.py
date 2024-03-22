def solution(n):
    answer = []
    def hanoi_tower(n,fromm,temp,to):
        if n == 1:
            answer.append([fromm,to])
        else:
            hanoi_tower(n-1,fromm,to,temp)
            answer.append([fromm,to])
            hanoi_tower(n-1,temp,fromm,to) 
    hanoi_tower(n,1,2,3)      
    return answer


    