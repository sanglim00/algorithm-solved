import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans_list = []

def BFS(graph_, visited, v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = 1

    cnt = 0
    while queue:
        now = queue.popleft()
        cnt += 1
        for i in range(4):
            py, px = now[0]+dy[i], now[1]+dx[i]
            if 0<=py<M and 0<=px<N:
                if not visited[py][px] and graph_[py][px] == 0:
                    queue.append([py, px])
                    visited[py][px] = 1

    ans_list.append(cnt)

graph_ = [[0 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]

lst = []
for _ in range(K):
    row = list(map(int, sys.stdin.readline().split()))
    lst.append(row)

for x1, y1, x2, y2 in lst:
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph_[i][j] = 1

ans = 0
for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph_[i][j] == 0:
            BFS(graph_, visited, (i, j))
            ans += 1

print(ans)
for i in sorted(ans_list): print(i, end=' ')
print()