import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int, sys.stdin.readline().split())

tomato = []
visited = [[0 for _ in range(M)] for _ in range(N)]

check = []
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(len(lst)):
        if lst[j] == 1:
            check.append((i, j))
    tomato.append(lst)


queue = deque([])
for i, j in check:
    queue.append((i, j, 0))


def BFS(graph_, visited):
    
    ans = 0
    while queue:
        now = queue.popleft()
        for i in range(4):
            py, px = dy[i]+now[0], dx[i]+now[1]
            if 0<=px<M and 0<=py<N:
                if not visited[py][px] and graph_[py][px] == 0:
                    visited[py][px] = 1
                    queue.append((py, px, now[2]+1))
        ans = now[2]
    return ans
        
ans_lst = []
for i in range(N): #row 
    for j in range(M): #col 
        if not visited[i][j] and tomato[i][j] == 1:
            ans_lst.append(BFS(tomato, visited))

check = False
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and tomato[i][j] == 0:
            check = True
            break
    if check: break

print(-1 if check else max(ans_lst))