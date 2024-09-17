import sys
from collections import deque

px = [1, -1, 0, 0]
py = [0, 0, 1, -1]

def BFS(graph_, visited, v, H, W):
    queue = deque([v])
    visited[v[0]][v[1]] = 1

    while queue:
        now = queue.popleft()
        
        for i in range(4):
            ny, nx = now[0]+py[i], now[1]+px[i]

            if 0<=ny<H and 0<=nx<W:
                if not visited[ny][nx] and graph_[ny][nx] == '#':
                    visited[ny][nx] = 1
                    queue.append((ny, nx))


T = int(sys.stdin.readline())
for _ in range(T):
    H, W = map(int, sys.stdin.readline().split())
    graph_ = []
    visited = [[0 for _ in range(W)] for _ in range(H)]

    for _ in range(H):
        lst = list(sys.stdin.readline().rstrip())
        graph_.append(lst)

    ans = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and graph_[i][j] == '#':
                BFS(graph_, visited, (i, j), H, W)
                ans += 1

    print(ans)