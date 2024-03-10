def solution(s):
    answer = []
    count = 0
    col_0 = 0
    while s != '1':
        num = s.count('1')
        col_0 += len(s) - num
        s = format(num,'b')
        count += 1
    
    return [count,col_0]