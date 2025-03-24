import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    lst = list(input().rstrip())
    graph.append(lst)

visited = [[0 for _ in range(N)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(pi, pj):
    queue = deque([(pi, pj)])
    visited[pi][pj] = 1

    while queue:
        now = queue.popleft()

        for i in range(4):
            ny, nx = now[0]+dy[i], now[1]+dx[i]

            if 0<=ny<N and 0<=nx<N:
                if not visited[ny][nx] and graph[ny][nx] == '*':
                    queue.append((ny, nx))
                    visited[ny][nx] = 1

ans = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == '*':
            ans += 1
            BFS(i, j)
            
print(ans)