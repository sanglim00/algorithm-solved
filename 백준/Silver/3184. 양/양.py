import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
graph_ = []
for _ in range(R):
    row = list(sys.stdin.readline().rstrip())
    graph_.append(row)

visited = [[0 for _ in range(C)] for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sheep, wolf = 0, 0
def BFS(v):
    queue = deque([v])
    global sheep, wolf

    s_cnt, w_cnt = 0, 0
    if graph_[v[0]][v[1]] == 'o': s_cnt += 1
    elif graph_[v[0]][v[1]] == 'v': w_cnt += 1

    while queue:
        now = queue.popleft()

        for i in range(4):
            ny, nx = now[0]+dy[i], now[1]+dx[i]

            if 0<=ny<R and 0<=nx<C:
                if not visited[ny][nx] and graph_[ny][nx] != '#':
                    if graph_[ny][nx] == 'o': s_cnt += 1
                    elif graph_[ny][nx] == 'v': w_cnt += 1

                    visited[ny][nx] = 1
                    queue.append((ny, nx))
    
    if s_cnt > w_cnt: sheep += s_cnt
    else: wolf += w_cnt    


for i in range(R):
    for j in range(C):
        if not visited[i][j] and graph_[i][j] != '#':
            visited[i][j] = 1
            BFS((i, j))

print(sheep, wolf)        