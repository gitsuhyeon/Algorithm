def solution(n):
    answer = ''
    front_124 = ['1','2','4']
    tn = n
    i = 1
    answer = front_124[(tn-1)%3] 
    while tn > 3**i:
            tn -= 3**i
            temp = ((tn-1) // 3**i) % 3
            answer = front_124[temp] +answer
            i += 1
    return answer
