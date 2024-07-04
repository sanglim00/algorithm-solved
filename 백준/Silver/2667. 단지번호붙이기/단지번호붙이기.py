import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans_list = []

def BFS(graph_, visited, v):
    queue = deque([(v)])
    visited[v[0]][v[1]] = 1
    
    check = 1
    while queue:
        now = queue.popleft()
        for i in range(4):
            py, px = now[0] + dy[i], now[1] + dx[i]
            if 0<=py<N and 0<=px<N:
                if not visited[py][px] and graph_[py][px] == '1':
                    queue.append((py, px))
                    visited[py][px] = 1
                    check += 1
    
    ans_list.append(check)

N = int(sys.stdin.readline())

graph_ = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    lst = list(sys.stdin.readline().rstrip())
    graph_.append(lst)

ans = 0 

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph_[i][j] == '1':
            BFS(graph_, visited, (i, j))
            ans += 1

print(ans)
ans_list.sort()
for i in ans_list: print(i)