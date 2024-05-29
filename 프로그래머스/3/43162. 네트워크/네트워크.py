def solution(n, computers):
    answer = 0
    dic = [[] for _ in range(n)]
    visited = [False]*n
    
    for i in range(len(computers)):
        for j in range(i+1,len(computers)):
            if computers[i][j] == 1:
                dic[i].append(j)
                dic[j].append(i)
                
    def dfs(t):
        visited[t] =True
        for s in dic[t]:
            if not visited[s]:
                dfs(s)
            
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
        
    return answer