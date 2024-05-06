def solution(triangle):
    answer = 0
    memo = {}
    idx = 0
    for n in range(len(triangle)-2,-1,-1):
        lenn = len(triangle[n])
        for m in range(lenn):
            idx += 1
            if n == len(triangle)-2:
                memo[idx] = triangle[n][m]+max(triangle[n+1][m],triangle[n+1][m+1])
            else:
                memo[idx] = triangle[n][m]+max(memo[idx-lenn-1],memo[idx-lenn])
              
    
    return memo[idx]
