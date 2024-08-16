import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

graph_ = []
visited = [[0 for _ in range(N+1)] for _ in range(M+1)]

for _ in range(M):
    row = list(map(int, sys.stdin.readline().split()))
    graph_.append(row)

px = [-1, -1, -1, 0, 0, 1, 1, 1]
py = [-1, 0, 1, -1, 1, -1, 0, 1]

def BFS(graph_, visited, v):
    queue = deque([v])
    visited[v[0]][v[1]] = 0

    while queue:
        now = queue.popleft()
        for i in range(8):
            ny, nx = now[0]+py[i], now[1]+px[i]
            if 0<=ny<M and 0<=nx<N:
                if not visited[ny][nx] and graph_[ny][nx] == 1:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
        
ans = 0           
for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph_[i][j] == 1:
            BFS(graph_, visited, (i, j))
            ans += 1

print(ans)