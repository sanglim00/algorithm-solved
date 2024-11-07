def BFS(graph, visited, v):
    visited[v] = 1
    queue = [v]
    
    while queue:
        now = queue.pop(0)
        
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
    

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j or computers[i][j] == 0: continue
            graph[i+1].append(j+1)
    
    visited = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if not visited[i]:  
            answer += 1
            BFS(graph, visited, i)
    
    
    return answer