import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)

visited = [[-1 for _ in range(M)] for _ in range(N)]

queue = deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 0

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]


while queue:
    now = queue.popleft()
    
    for i in range(8):
        ny, nx = now[0]+dy[i], now[1]+dx[i]

        if 0<=ny<N and 0<=nx<M:
            if visited[ny][nx] == -1:
                visited[ny][nx] = visited[now[0]][now[1]]+1
                queue.append((ny, nx))

ans = 0
for i in visited:
    ans = max(ans, max(i))
print(ans)