from collections import deque

def BFS(graph_, visited, v):
    queue = deque([v])
    visited[v] = 0
    
    while queue:
        now = queue.popleft()
        for i in graph_[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[now] + 1
        
        
def solution(n, vertex):
    answer = 0
    
    graph_ = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    
    for start, end in vertex:
        graph_[start].append(end)
        graph_[end].append(start)
    
    for i in graph_: i.sort()
    
    BFS(graph_, visited, 1)
    
    for i in range(len(visited)):
        if i != 1 and visited[i] == max(visited):
            answer += 1
    
    return answer