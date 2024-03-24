import math
def solution(n):
    answer = 1
    tn , tr = n//2 , n % 2
    if n >1:
        answer += 1
    if n % 2 == 1:
        answer += tn
    while tn > 1:
        tn -= 1
        tr = n- (2 * tn)
        answer += math.comb(tn+tr,tn)
    return answer %1234567
