import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(grahp_, visited, v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = 1
    
    while queue:
        now = queue.popleft()
        for i in range(4):
            py, px = now[0] + dy[i], now[1] + dx[i]
            if 0<=py<N and 0<=px<M:
                if not visited[py][px] and grahp_[py][px] == 1:
                    queue.append((py, px))
                    visited[py][px] = 1


T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    grahp_ = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for j in range(K):
        px, py = map(int, sys.stdin.readline().split())
        grahp_[py][px] = 1
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and grahp_[i][j] == 1:
                BFS(grahp_, visited, (i, j))
                ans += 1
    
    print(ans)
