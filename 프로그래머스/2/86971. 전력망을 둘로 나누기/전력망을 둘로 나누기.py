def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(node, parent):
        count = 1
        for child in graph[node]:
            if child != parent:
                count += dfs(child,node)
        return count
    
    minimum = n
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        minimum = min(abs(2*dfs(a,b)-n),minimum)
    
        graph[a].append(b)
        graph[b].append(a)
        
    return minimum