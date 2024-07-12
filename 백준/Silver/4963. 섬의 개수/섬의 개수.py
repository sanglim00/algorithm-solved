import sys
from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

w, h = 0, 0

def BFS(graph_, visited, v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = 1

    while queue:
        now = queue.popleft()

        for i in range(8):
            py, px = now[0]+dy[i], now[1]+dx[i]
            if 0<=py<h and 0<=px<w:
                if not visited[py][px] and graph_[py][px] == 1:
                    queue.append((py, px))
                    visited[py][px] = 1

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0: break
        
    graph_ = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    
    for i in range(h):
        lst = list(map(int, sys.stdin.readline().split()))
        graph_.append(lst)
    
    ans = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph_[i][j] == 1:
                BFS(graph_, visited, (i, j))
                ans += 1
    print(ans)