import sys
from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def BFS(graph_, visited, v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = 1

    check = True
    while queue and check:
        now = queue.popleft()
        for i in range(8):
            py, px = now[0]+dy[i], now[1]+dx[i]
            if 0<=py<l and 0<=px<l:
                if not visited[py][px] and graph_[py][px] == 0:
                    queue.append((py, px))
                    visited[py][px] = 1
                    graph_[py][px] = graph_[now[0]][now[1]] + 1

            if py == y2 and px == x2:
                print(graph_[py][px]) 
                check = False 
                break         


T = int(sys.stdin.readline())

for _ in range(T):
    l = int(sys.stdin.readline())
    y1, x1 = map(int, sys.stdin.readline().split())
    y2, x2 = map(int, sys.stdin.readline().split())

    graph_ = [[0 for _ in range(l)] for _ in range(l)]
    visited = [[0 for _ in range(l)] for _ in range(l)]

    BFS(graph_, visited, (y1, x1))