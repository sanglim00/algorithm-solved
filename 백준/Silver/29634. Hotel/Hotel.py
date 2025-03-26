import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(graph, visited, i, j):
    queue = deque([(i, j)])
    visited[i][j] = 1

    cnt = 0
    while queue:
        now = queue.popleft()
        cnt += 1

        for i in range(4):
            ny, nx = now[0]+dy[i], now[1]+dx[i]

            if 0<=ny<N and 0<=nx<M:
                if not visited[ny][nx] and graph[ny][nx] == '.':
                    queue.append((ny, nx))
                    visited[ny][nx] = 1

    return cnt

N, M = map(int, input().split())
graph = []


for i in range(N):
    lst = list(input().rstrip())
    graph.append(lst)

visited = [[0 for _ in range(M)] for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == '.':
            now = BFS(graph, visited, i, j)
            ans = max(ans, now)

print(ans if ans else -1)