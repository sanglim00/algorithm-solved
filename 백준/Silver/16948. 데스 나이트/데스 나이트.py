import sys
from collections import deque

N = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

px = [-1, 1, -2, 2, -1, 1]
py = [-2, -2, 0, 0, 2, 2]

def BFS(graph_, visited, v):
    queue = deque([v])
    visited[v[0]][v[1]] = 0

    check = True
    while queue and check:
        now = queue.popleft()
        for i in range(6):
            ny, nx = now[0]+py[i], now[1]+px[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[ny][nx]:
                    visited[ny][nx] = visited[now[0]][now[1]] + 1
                    queue.append((ny, nx))
        
            
graph_ = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]

graph_[r1][c1] = 9
graph_[r2][c2] = 8


BFS(graph_, visited, (r1, c1))
print(visited[r2][c2] if visited[r2][c2] else -1)