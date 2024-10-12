import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

graph_ = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        lst = list(map(int, sys.stdin.readline().split()))
        graph_[i].append(lst)

visited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

flag = False
def BFS():
    global flag
    queue = deque([])

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph_[i][j][k] == 1:
                    queue.append((i, j, k))
                    visited[i][j][k] = 0
                elif graph_[i][j][k] == 0: 
                    flag = True
                else: 
                    visited[i][j][k] = 101

    if not flag: return

    while queue:
        now = queue.popleft()

        for i in range(6):
            nz, ny, nx = now[0]+dz[i], now[1]+dy[i], now[2]+dx[i]

            if 0<=nz<H and 0<=ny<N and 0<=nx<M:
                if visited[nz][ny][nx] == -1 and graph_[nz][ny][nx] == 0:
                    visited[nz][ny][nx] = visited[now[0]][now[1]][now[2]] + 1
                    queue.append((nz, ny, nx))

BFS()

if flag:
    ans = -1
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k] == -1: 
                    print(-1)
                    exit()
                elif visited[i][j][k] != 101: 
                    ans = max(ans, visited[i][j][k])
    print(ans)
else: 
    print(0)