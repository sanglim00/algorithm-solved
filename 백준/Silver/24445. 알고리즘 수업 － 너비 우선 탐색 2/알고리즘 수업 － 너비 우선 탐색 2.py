import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph_ = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph_[u].append(v)
    graph_[v].append(u)

for i in graph_: i.sort(reverse=True)

idx = 1
def BFS(v):
    global idx

    queue = deque([v])
    visited[v] = idx

    while queue:
        now = queue.popleft()

        for i in graph_[now]:
            if not visited[i]:
                idx += 1
                visited[i] = idx
                queue.append(i)
                
BFS(R)
for i in range(1, N+1): print(visited[i])