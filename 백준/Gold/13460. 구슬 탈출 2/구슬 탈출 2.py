import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

graph_ = []
for _ in range(N):
    lst = list(sys.stdin.readline().rstrip())
    graph_.append(lst)

ry, rx, by, bx = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if graph_[i][j] == "R": 
            ry, rx = i, j
        if graph_[i][j] == "B":
            by, bx = i, j

px = [1, -1, 0, 0]
py = [0, 0, 1, -1]

ans = -1
def BFS():
    global ans
    cnt = 0
    queue = deque([(ry, rx, by, bx, cnt)])
    visited[ry][rx][by][bx] = 1

    while queue:
        now = queue.popleft()
        if now[4] > 10: 
            break
        if graph_[now[0]][now[1]] == 'O' and graph_[now[2]][now[3]] != 'O': 
            ans = now[4]
            break 

        for i in range(4):
            next_ry, next_rx = now[0], now[1]
            next_by, next_bx = now[2], now[3]
            while True:
                if graph_[next_ry][next_rx] != '#' and graph_[next_ry][next_rx] != 'O':
                    next_ry += py[i]
                    next_rx += px[i]
                else:
                    if graph_[next_ry][next_rx] == '#':
                        next_ry -= py[i]
                        next_rx -= px[i] 
                    break
            while True:
                if graph_[next_by][next_bx] != '#' and graph_[next_by][next_bx] != 'O':
                    next_by += py[i]
                    next_bx += px[i]
                else:
                    if graph_[next_by][next_bx] == '#':
                        next_by -= py[i]
                        next_bx -= px[i] 
                    break
            
            if next_ry == next_by and next_rx == next_bx:
                if graph_[next_ry][next_rx] != 'O':
                    red_dist = abs(now[0]-next_ry) + abs(now[1]-next_rx)
                    blue_dist = abs(now[2]-next_by) + abs(now[3]-next_bx)
                    if red_dist > blue_dist:
                        next_ry -= py[i]
                        next_rx -= px[i] 
                    else:
                        next_by -= py[i]
                        next_bx -= px[i] 
            
            if not visited[next_ry][next_rx][next_by][next_bx]:
                visited[next_ry][next_rx][next_by][next_bx] = 1
                queue.append((next_ry, next_rx, next_by, next_bx, now[4]+1))

BFS()
print(ans)