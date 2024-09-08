from collections import deque

px = [1, -1, 0, 0]
py = [0, 0, 1, -1]

def BFS(graph_, visited, v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = 1
    
    while queue:
        now = queue.popleft()
        
        for i in range(4):
            ny, nx = now[0]+py[i], now[1]+px[i]
            
            if 0<=ny<len(graph_) and 0<=nx<len(graph_[0]):
                if not visited[ny][nx] and graph_[ny][nx] == 1:
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[now[0]][now[1]] + 1
                    
                    if ny == len(graph_)-1 and nx == len(graph_[0])-1: break

def solution(maps):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    BFS(maps, visited, (0, 0))

    return visited[len(maps)-1][len(maps[0])-1] if visited[len(maps)-1][len(maps[0])-1] != 0 else -1