import sys
from collections import deque

N = int(sys.stdin.readline())

graph_ = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    graph_.append(lst)

def BFS(v):
    queue = deque([v])
    visited[v[0]][v[1]] = 1

    while queue:
        now = queue.popleft()
        num = graph_[now[0]][now[1]]
        
        if num == -1: break
        
        for i in ['l', 'r', 't', 'b']:
            ny, nx = now[0], now[1]
            if i == 'l': nx -= num
            elif i == 'r': nx += num
            elif i == 't': ny -= num
            else: ny += num

            if 0<=ny<N and 0<=nx<N:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
                
BFS((0, 0))
print('HaruHaru' if visited[-1][-1] else 'Hing')