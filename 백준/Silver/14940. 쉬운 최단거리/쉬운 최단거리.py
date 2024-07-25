import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph_ = []
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(graph_, visited, v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = 0

    while queue:
        now = queue.popleft()

        for i in range(4):
            py, px = now[0]+dy[i], now[1]+dx[i]
            if 0<=py<N and 0<=px<M:
                if not visited[py][px] and graph_[py][px] == 1:
                    queue.append((py, px))
                    visited[py][px] = visited[now[0]][now[1]] + 1

x, y = 0, 0
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(len(row)):
        if row[j] == 2:
            y = i
            x = j
    graph_.append(row)

BFS(graph_, visited, (y, x))

for i in range(N):
    for j in range(M):
        if graph_[i][j] != 0  and visited[i][j] == 0: 
            visited[i][j] = -1

visited[y][x] = 0

for i in range(N):
    for j in range(M):
        print(visited[i][j], end=' ')
    print()