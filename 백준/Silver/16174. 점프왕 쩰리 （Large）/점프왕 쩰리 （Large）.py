import sys
from collections import deque

N = int(sys.stdin.readline())

graph_ = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    graph_.append(row)

def BFS(graph_, visited, v):
    queue = deque([v])
    visited[v[0]][v[1]] = 0

    while queue:
        now = queue.popleft()
        dy = [graph_[now[0]][now[1]], 0]
        dx = [0, graph_[now[0]][now[1]]]
        for i in range(2):
            ny, nx = now[0]+dy[i], now[1]+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] = 1


BFS(graph_, visited, (0, 0))
print('HaruHaru' if visited[N-1][N-1] else 'Hing')
