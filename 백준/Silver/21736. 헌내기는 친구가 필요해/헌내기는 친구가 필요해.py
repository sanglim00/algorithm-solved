import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph_ = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(graph_, visited, v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = 1

    ans = 0
    while queue:
        now = queue.popleft()
        for i in range(4):
            ny, nx = now[0]+dy[i], now[1]+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if not visited[ny][nx] and graph_[ny][nx] != 'X':
                    queue.append((ny, nx))
                    visited[ny][nx] = 1   
                    if graph_[ny][nx] == 'P':
                        ans += 1  

    print(ans if ans else 'TT')

x, y = 0, 0
for i in range(N):
    row = list(sys.stdin.readline().strip())
    for j in range(len(row)):
        if row[j] == "I":
            y = i
            x = j
    graph_.append(row)

visited = [[0 for _ in range(M)] for _ in range(N)]
BFS(graph_, visited, (y, x))