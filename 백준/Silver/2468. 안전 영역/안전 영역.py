import sys
from collections import deque

N = int(sys.stdin.readline())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(graph_, visited, v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = 1

    while queue:
        now = queue.popleft()

        for i in range(4):
            py, px = now[0]+dy[i], now[1]+dx[i]
            if 0<=py<N and 0<=px<N:
                if not visited[py][px] and graph_[py][px] == 1:
                    queue.append((py, px))
                    visited[py][px] = 1

graph_ = []
MAX = 1

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    MAX = max(row)
    graph_.append(row)

ans = 0
for cnt in range(0, MAX):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    ground = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if graph_[i][j] <= cnt:
                ground[i][j] = 0
            else: 
                ground[i][j] = 1

    check = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and ground[i][j] == 1:
                BFS(ground, visited, (i, j))
                check += 1
    ans = max(ans, check)

print(ans)